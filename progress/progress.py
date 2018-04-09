from flask import Flask, render_template
from flask_api import FlaskAPI
from pdb import *
import json

progressAPI = FlaskAPI(__name__)


@progressAPI.route('/')
def hello_world():
    author = "butt"
    name = "a butt"
    return "a butt"


@progressAPI.route('/api/playtime/')
@progressAPI.route('/api/playtime/<p>/')
def Playtime(p=None):
    butt=ButtDbInterface()
    if p:
        playtime = butt.playtime_single(p)
        a=[]
        a.append({"player": p, "playtime": playtime[0], "sessions": playtime[1]})

        return flask.jsonify({"playtime": a})

    else:
        return flask.jsonify({"playtime": butt.playtime_global()})


if __name__ == '__main__':
    progressAPI.run()
