from flask import Flask
app = Flask(__name__)

@app.route("/")
def ping():
    return "Here we go!"

@app.route("/hello")
def hello():
    return "Hello from the server side!"

@app.route("/bye")
def bye():
    return "Byee!"

@app.route("/hello/<name>")
def helloWithName(name):
    return "Hello " + name + "!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)