from flask import Flask

app = Flask(__name__)

@app.route("/")
def hw():
    return "hello world!"

app.run(port=9999)