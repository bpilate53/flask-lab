from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<p>Hello World</p>"

@app.route("/heaven")
def hello_heaven():
    return "<p>Hello from the Heaven</p>"
