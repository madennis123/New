from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def index():
    return "<h1> This is the Home Page for Web-app2 </h1>"

@application.route("/profile/<name>")
def profile(name):
    return render_template("profile.html" , name=name) 	

if __name__ == "__main__":
    application.run()
