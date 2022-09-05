#!/usr/bin/python3
""" Task 5 """
from flask import Flask, abort
from flask import render_template

app = Flask(__name__)
"""starts a Flask web application"""
app.url_map.strict_slashes = False


@app.route("/")
def hello_route():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_route2():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def hello_route3(text):
    """ display 'C' followed by the value of the text variable"""
    text2 = 'C {}'.format(text.replace('_', ' '))
    return text2


@app.route("/python/")
@app.route("/python/<text>")
def hello_route4(text='is cool'):
    """display 'Python', followed by the value of the text variable"""
    text2 = 'Python {}'.format(text.replace('_', ' '))
    return text2


@app.route("/number/<n>")
def hello_route5(n):
    """  display 'n is a number' only if n is an integer """

    try:
        text = int(n)
        text2 = '{} is a number'.format(n)
        return text2
    except:
        abort(404)


@app.route("/number_template/<n>")
def hello_route6(n):
    """ display a HTML page only if n is an integer """
    try:
        return render_template('5-number.html', num=int(n))
    except:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
