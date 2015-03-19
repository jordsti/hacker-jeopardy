from ..service_func import service_func, func_error, meta_arg


class remove_team(service_func):
    def __init__(self):
        service_func.__init__(self, "/team/remove")
        self.name = "Remove team"
        self.description = "Remove a team from the Jeopardy Game"
        self.args.append(meta_arg("key", "Protection key", "none"))
        self.args.append(meta_arg("team", "Team id to remove", "none"))

    def execute(self, args, server):
        key = args["key"]
        team = int(args["team"])
        if server.key == key:
            teams = server.game_data.teams
            server.game_data.teams = []
            for t in teams:
                if not t.id == team:
                    server.game_data.teams.append(t)
        else:
            raise func_error("Key is invalid")

    def answer(self):
        data = {}
        return data