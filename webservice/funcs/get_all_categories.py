from ..service_func import service_func, func_error, meta_arg

class get_all_categories(service_func):
    def __init__(self):
        service_func.__init__(self, '/category/all')
        self.name = "Get all categories"
        self.description = "Get all categories with id for current Jeopardy"
        self.cats = None

    def execute(self, args, server):
        self.cats = server.game_data.categories

    def answer(self):
        data = {"categories": []}
        for c in self.cats:
            data["categories"].append([c.id, c.name])
        return data