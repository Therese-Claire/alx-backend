#!/usr/bin/env python3
"""basic babel setup in our simple flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """language config for our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determines the best match with our supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.est_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """default route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
