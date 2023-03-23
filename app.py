from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from qa, sz0711"
