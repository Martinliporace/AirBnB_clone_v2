#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)
"""starts a Flask web application"""
app.url_map.strict_slashes = False


@app.route("/")
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_route2():
    return "HBNB"


@app.route("/c/<text>")
def hello_route3(text):
    text2 = 'C {}'.format(text.replace('_', ' '))
    return text2


@app.route("/python/")
@app.route("/python/<text>")
def hello_route4(text='is cool'):
    text2 = 'Python {}'.format(text.replace('_', ' '))
    return text2


@app.route("/number/<n>")
def hello_route5(n):
    text = int(n)
    text2 = '{} is a number'.format(n)
    return text2


@app.route("/number_template/<n>")
def hello_route6(n):
    num = int(n)
    if type(num) is int:
        return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
