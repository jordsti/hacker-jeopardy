import urllib2
import json

class http_client:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def __request(self, req_url):
        url = "http://%s:%d/%s" % (self.hostname, self.port, req_url)

        req = urllib2.urlopen(url)
        data = req.read()
        return data

    def get_functions(self):
        data = self.__request("")
        if len(data) > 0:
            return json.loads(data)

    def get_teams(self):
        data = self.__request("team/all")
        if len(data) > 0:
            return json.loads(data)

    def get_game_state(self):
        data = self.__request("game/state")
        if len(data) > 0:
            return json.loads(data)

    def get_categories(self):
        data = self.__request("category/all")
        if len(data) > 0:
            return json.loads(data)

    def get_points_table(self):
        data = self.__request("points/table")
        if len(data) > 0:
            return json.loads(data)

    def get_categories_ranks(self):
        data = self.__request("category/ranks")
        if len(data) > 0:
            return json.loads(data)