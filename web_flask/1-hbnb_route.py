#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""starts a Flask web application"""
app.url_map.strict_slashes = False


@app.route("/")
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_route2():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
