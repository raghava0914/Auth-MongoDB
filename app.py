from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from auth import signup_user, login_user
from config import SECRET_KEY, SESSION_TYPE

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_TYPE"] = SESSION_TYPE
Session(app)

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        msg = signup_user(email, password)
        return render_template("signup.html", message=msg)
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        msg = login_user(email, password)
        if "successful" in msg:
            return redirect(url_for("dashboard"))
        return render_template("login.html", message=msg)
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
