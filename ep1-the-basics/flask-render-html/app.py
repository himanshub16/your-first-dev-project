from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)

@app.route("/hello")
def helloAnonymous():
    return hello("Anonymous")

if __name__ == '__main__':
    app.run(debug=True, port=5000)