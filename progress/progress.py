from flask import Flask, render_template
from flask_api import FlaskAPI

progressAPI = FlaskAPI(__name__)


@progressAPI.route('/')
def hello_world():
    author = "butt"
    name = "a butt"
    return "a butt"


@progressAPI.route('/api/playtime/<p>/')
def Playtime(p):
    return {p: 'You'}





if __name__ == '__main__':
    progressAPI.run()
