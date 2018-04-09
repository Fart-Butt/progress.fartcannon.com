import urllib.request, json, urllib.error, http.client
import datetime, flask.json
from butt_database import *


class ButtDbInterface:
    def __init__(self):
        self.players = []
        self.db = db()



    def config(self, url, mode):
        self.updateurl = url
        self.master_config = mode



    def playtime_global(self):
        players = self.db.do_query(
            "select player, cast(abs(sum(timedelta)) as UNSIGNED) as seconds, count(timedelta) as sessions from progress_playertracker_v2 group by player")
        return players

    def playtime_single(self, player):
        time = self.db.do_query(
            "select sum(timedelta) as seconds, count(timedelta) as sessions from progress_playertracker_v2 where player=%s",
            player)
        return [int(time[0]['seconds']), time[0]['sessions']]

