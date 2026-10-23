from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Assignment 3 Web Application!"

 app.run(host="0.0.0.0", port=5000)
