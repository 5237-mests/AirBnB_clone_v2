#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display1():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display2():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display3(text):
    return 'C ' + str(text).replace("_", " ")


@app.route('/python/<text2>', strict_slashes=False)
def display4(text2):
    return 'Python ' + str(text2).replace("_", " ")


@app.route('/python/', defaults={'text3': 'is cool'},  strict_slashes=False)
def display5(text3):
    return 'Python ' + str(text3).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display6(n):
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display7(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display8(n):
    numoddev = ''
    if(n % 2 == 0):
        numoddev = 'even'
    else:
        numoddev = 'odd'
    return render_template('6-number_odd_or_even.html', oddev=numoddev, num=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)