from ..service_func import service_func, func_error, meta_arg


class get_points_table(service_func):
    def __init__(self):
        service_func.__init__(self, "/points/table")
        self.name = "Get points table"
        self.description = "Return the table of points by rank"
        self.ranks = []

    def init(self):
        self.ranks = []

    def execute(self, args, server):
        ir = 0
        for r in server.game_data.points_table.points:
            self.ranks.append({"id": ir, "points": r})
            ir += 1

    def answer(self):
        data = {
            "ranks": self.ranks
        }
        return data