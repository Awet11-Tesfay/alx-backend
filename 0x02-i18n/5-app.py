#!/usr/bin/env python3
""" Force locale with URL parameter
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Function with the babel.localeselector decorator
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Function that returns a user dictionary or None
    """
    userId = request.args.get('login_as, None')
    if userId is not None and int(userId) in users.keys():
        return users.get(int(userId))
    return None


@app.before_request
def before_request():
    """ To find a user if any and set it as a global on
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run()
