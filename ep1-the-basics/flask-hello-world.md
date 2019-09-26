# Hello World using Flask

Install flask
```bash
pip3 install flask
```
---

Open any editor and save the code snippet below as - `hello.py`.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

Open your terminal and run `python3 hello.py`.

The output should contain a statement containing `http://127.0.0.1:5000`.

Visit this URL in your browser and try playing with the `hello()` function to see how things change.

**What's happening here?**

`from flask import Flask
app = Flask(__name__)
`

This creates a new object of type Flask. In other words, this creates a new variable app, on which we call certain linked methods as `app.run`, `app.route` etc.

`@app.route` wires the specific route to the particular function.
