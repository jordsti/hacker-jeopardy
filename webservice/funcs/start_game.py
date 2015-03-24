from ..service_func import service_func, func_error, meta_arg


class start_game(service_func):
    def __init__(self):
        service_func.__init__(self, "/game/start")
        self.name = "Start Game"
        self.description = "Start a new game, need correct number of teams (4)"
        self.args.append(meta_arg("key", "Protection Key", "none"))

    def execute(self, args, server):

        key = args["key"]
        # tired of doing this check, maybe implement a classic check_key into service_func
        if server.key == key:
            if not server.game_data.game_on:
                if len(server.game_data.teams) == 4: # remove this hardcoded team count ? but jeopardy need 4 teams ?
                    server.game_data.start_game()
                else:
                    raise func_error("Only %d teams are registered, need 4" % len(server.game_data.teams))
            else:
                raise func_error("Game already started")

        else:
            raise func_error("Invalid key")