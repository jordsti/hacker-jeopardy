from ..service_func import service_func, func_error, meta_arg


class get_game_state(service_func):
    def __init__(self):
        service_func.__init__(self, "/game/state")
        self.name = "Get current game state"
        self.description = "Get the current game state with the state definition"
        # no args

        self.data = None

    def init(self):
        self.data = None

    def execute(self, args, server):

        self.data = {
            "game_on": server.game_data.game_on,
            "state": server.game_data.state,
            "defs": server.game_data.get_game_states()
        }

    def answer(self):
        return self.data