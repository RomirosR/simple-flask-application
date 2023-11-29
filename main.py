from flask import Flask, render_template, request, url_for, flash, redirect, session
import json

app = Flask(__name__)
app.secret_key = "asdasdasdasd"

@app.route("/", methods=("GET", "POST"))
def main():
    if request.method == "POST":
        name = request.form['name']
        session['name'] = name
        return redirect(url_for(".hello"))
    return render_template("main.html")

@app.route("/hello/")
def hello():
    return render_template("hello.html", name=session['name'])