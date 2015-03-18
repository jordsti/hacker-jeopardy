from ..service_func import service_func, func_error, meta_arg

class add_team(service_func):
    def __init__(self):
        service_func.__init__(self, "/team/add")
        self.name = "Add team"
        self.description = "Add a new team to the jeopardy"
        self.args.append(meta_arg("key", "Protection Key", "none"))
        self.args.append(meta_arg("name", "New Team Name", "none"))
        self.team = None

    def init(self):
        self.team = None

    def execute(self, args, server):
        key = args["key"]
        name = args["name"]

        if key != server.key:
            raise func_error("Invalid key")
        else:

            for t in server.game_data.teams:
                if t.name == name:
                    raise func_error("Team name already exists")

            new_team = server.game_data.new_team(name)
            self.team = new_team

    def answer(self):
        #returning new team id
        data = {"team_id": self.team.id}
        return data