from ..service_func import service_func, func_error, meta_arg


class get_categories_rank(service_func):
    def __init__(self):
        service_func.__init__(self, "/category/ranks")
        self.name = "Get categories ranks"
        self.description = "-"

        self.cats = []

    def init(self):
        self.cats = []

    def execute(self, args, server):
        for c in server.game_data.categories:
            cat = {
                "id": c.id,
                "name": c.name,
                "ranks_available": []
            }

            for r in c.ranks_available:
                cat["ranks_available"].append(r)

            self.cats.append(cat)

    def answer(self):
        data = {
            'categories': self.cats
        }
        return data