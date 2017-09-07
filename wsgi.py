from flask import Flask, render_template
application = Flask(__name__)

@application.route("/profile/<name>")
def profile(name):
    return render_template("profile.html" , name=name) 	

if __name__ == "__main__":
    application.run()
