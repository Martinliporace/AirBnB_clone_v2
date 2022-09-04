#!/usr/bin/python3
"""task 2"""
from flask import Flask

app = Flask(__name__)
"""starts a Flask web application"""
app.url_map.strict_slashes = False


@app.route("/")
def hello_route():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_route2():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def hello_route3(text):
    """ display 'C' followed by the value of the text variable"""
    text2 = 'C {}'.format(text.replace('_', ' '))
    return text2


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
