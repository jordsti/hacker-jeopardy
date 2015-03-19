from ..service_func import service_func, func_error, meta_arg


class add_point_to_team(service_func):
    def __init__(self):
        service_func.__init__(self, "/team/addpoint")
        self.name = "Add point to team"
        self.description = "Add point to a team corresponding by it team id"
        self.args.append(meta_arg("key", "Protection key", "none"))
        self.args.append(meta_arg("team", "Team Id", "none"))
        self.args.append(meta_arg("point", "Point to add", "none"))

    def execute(self, args, server):
        key = args["key"]
        point = int(args["point"])
        team = int(args["team"])

        if server.key == key:
            t = server.game_data.get_team(team)
            if t is not None:
                t.points += point
        else:
            raise func_error("Invalid key")