#!/usr/bin/python3
"""
START TO USE FLASK.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
