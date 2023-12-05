from flask import Flask , render_template,url_for,flash,redirect
from flask_sslify import SSLify
from forms import RegistrationForm,LoginForm
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
    return render_template('index.html',posts=posts)
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

    # app.run(ssl_context=('hostcert.pem', 'hostkey.pem'),debug=True,host='0.0.0.0')