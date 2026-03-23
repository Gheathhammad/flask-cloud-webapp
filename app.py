import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello from Gheath Docker App!"

@app.route('/how are you')
def hello():
    return "I am doing great! This app is running inside Docker"

@app.route("/about")
def about():
    return "This is a Flask app containerized using Docker"

if __name__ == "__main__":
    port = int(os.environ.get("PORT",8080))
    app.run(host="0.0.0.0", port=8080)
