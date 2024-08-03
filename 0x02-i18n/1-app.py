#!/usr/bin/env python3
"""basic babel setup in the flask app"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """language config for our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """default route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
