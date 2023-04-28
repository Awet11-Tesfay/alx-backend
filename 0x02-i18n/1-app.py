#!/usr/bin/env python3
""" Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configure the available languages and time
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.debug = True
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """ The returned html file
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
