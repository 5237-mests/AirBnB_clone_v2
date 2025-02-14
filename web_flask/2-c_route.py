#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display1():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display2():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display3(text):
    # mystring = str(text)
    return 'C ' + str(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
