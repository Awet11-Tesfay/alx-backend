#!/usr/bin/env python3
""" Force locale with URL parameter
"""
from flask import Flask, render_template, request
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
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Function with the babel.localeselector decorator
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
