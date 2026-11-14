import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, static_url_path='/static', static_folder='public/static')
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-key")

DUMMY_CONTRACT_ADDRESS = "0x0000000000000000000000000000000000000000"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contract_info")
def contract_info():
    return render_template("contract_info.html", CONTRACT_ADDRESS=DUMMY_CONTRACT_ADDRESS)

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Preview Mode: Authentication backend not included in demo build.", "warning")
        return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        flash("Preview Mode: Institution registration backend not included in demo build.", "warning")
        return redirect(url_for("register"))
    return render_template("register.html")

@app.route("/issue")
def issue():
    return render_template("issue.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        flash("Preview Mode: AI & Blockchain verification engine is offline in this build.", "warning")
        return redirect(url_for("verify"))
    return render_template("verify.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)