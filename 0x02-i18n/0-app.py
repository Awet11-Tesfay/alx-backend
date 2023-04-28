#!/usr/bin/python3
""" Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    """ The html function that will returned
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
