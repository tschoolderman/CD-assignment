from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/trap")
def lon():
    return render_template("trap.html", title="You were warned...")


@app.route("/magic", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    else:
        return render_template("magic.html", title="Magic")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")
