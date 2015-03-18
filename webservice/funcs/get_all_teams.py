from ..service_func import service_func, func_error, meta_arg

class get_all_teams(service_func):
    def __init__(self):
        service_func.__init__(self, "/team/all")
        self.name = "Get all teams"
        self.description = "Get all teams with id for current Jeopardy"
        self.teams = []

    def execute(self, args, server):
        self.teams = server.game_data.teams

    def answer(self):
        data = {"teams": []}
        for t in self.teams:
            team = {"id": t.id, "name": t.name, "points": t.points}
            data["teams"].append(team)

        return data
