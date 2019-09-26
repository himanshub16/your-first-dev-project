from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-double", methods=["POST"])
def getDouble():
    number = int(request.form["entered-value"])
    value = number * 2
    return render_template("result.html", initial_value=number, double_value=value)


if __name__ == '__main__':
    app.run(debug=True, port=5000)