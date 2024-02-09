from flask import Flask , render_template,request,jsonify
import os,base64
import cv2
import numpy as np
from ultralytics import YOLO
import localisator
import mapper
model =YOLO('./static/best (2).pt')
classes=[]


app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    current_url=request.url
    return render_template('index.html',current_url=current_url)
@app.route("/video")
def video():
    return render_template("video.html")

@app.route("/process_frame", methods=['POST'])
def process_frame():
    if request.method == 'POST':
        frame_data = request.json['frameData']
        # Decode the base64 image data
        if frame_data:
            img_data = frame_data.split(',')[1].encode('utf-8')
            img_binary = np.frombuffer(base64.b64decode(img_data), np.uint8)
            
            # Decode the image using OpenCV
            frame = cv2.imdecode(img_binary, cv2.IMREAD_COLOR)
            class_names=model.names
            # Process the frame with YOLO
            results = model(frame)
            for r in results:
                boxes=r.boxes
                for box in boxes:
                    if box :
                        x1,y1,x2,y2 = box.xyxy[0]
                        x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.putText(frame,class_names[int(box.cls)]+" "+str(round(float(box.conf),2)),(x1+20,y1+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
                        if round(float(box.conf),2)>0.5:
                            classes.append(class_names[int(box.cls)])
            # Encode the image to base64 for sending back to the client
            frame1 = cv2.imencode('.jpg', frame,[int(cv2.IMWRITE_JPEG_QUALITY), 2])[1].tobytes()
            base64_image = base64.b64encode(frame1).decode('utf-8')

            return jsonify({'frameData':base64_image})
@app.route("/localisation", methods=['POST'])
def localisation():
        global classes
        a=0
        if len(classes) > 10: #the number 20 to consider by test!!!
            unique_classes = localisator.remove_occurrences(classes)
            a= localisator.localisate(unique_classes)
            classes = []
        if a!=0:
            stri=mapper.map(a)
        else:
            stri='../static/png2jpg/map.jpg'
        # Encode the image to base64 for sending back to the client
        return jsonify({'msg':stri})

@app.route("/map")
def map():
    return render_template("map.html")
@app.route("/google")
def google():
    return render_template("google.html")

if __name__== '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')