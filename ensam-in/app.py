from flask import Flask , render_template,url_for,flash,redirect,request
from forms import RegistrationForm,LoginForm
import os
app = Flask(__name__)
# sslify=SSLify(app)
app.config['SECRET_KEY'] = 'ffc6ccfd8381224caa809c3e3d622748'
posts = [
    {
        'author': 'Mr.Massrour',
        'title': 'CLUB EVENTS ORGANISE UNE KEBAB PARTY AU 450',
        'content': 'First post content',
        'date_posted': 'April 20, 2030'
    },
    {
        'author': 'Allakouch',
        'title': 'Ensam opens at 7h closes at 8h30',
        'content': 'Second post content',
        'date_posted': 'April 21, 2026'
    }
]


@app.route("/")
@app.route("/home")
def home():
    current_url=request.url
    return render_template('index.html',posts=posts,current_url=current_url)
@app.route("/video")
def video():
    return render_template("video.html")

@app.route("/register", methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('video'))
    return render_template('register.html',title = 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title = 'Login', form=form)
if __name__== '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')