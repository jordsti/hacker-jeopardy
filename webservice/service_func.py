__author__ = 'jguerin'
import meta_func
import random

class func_error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


class service_func:

    def __init__(self, func_path):
        self.func_path = func_path
        self.description = ""
        self.name = ""
        self.args = [] #args must be of type meta_arg

    def execute(self, args, server):
        pass

    def answer(self):
        pass

    def get_meta(self):
        meta = meta_func.meta_func(self.func_path)
        meta.description = self.description
        meta.name = self.name
        meta.args = self.args
        return meta.to_dict()


class default_func(service_func):
    def __init__(self, functions):
        self.functions = functions
        service_func.__init__(self, '/')
        self.name = "Functions List"
        self.description = "Give a list of all availables functions"

    def answer(self):
        metas = []
        for f in self.functions:
            metas.append(f.get_meta())
        return {'functions': metas, 'version': 0}

class ask_question(service_func):
    def __init__(self):
        service_func.__init__(self, '/question/ask')
        self.name = "Ask Question"
        self.description = "Ask a question to a team, with a category id and a rank"
        self.question = None
        self.points = 0
        self.args.append(meta_func.meta_arg("key", "Protection Key", "none"))
        self.args.append(meta_func.meta_arg("category", "Category Id", "none"))
        self.args.append(meta_func.meta_arg("rank", "Rank Id", "none"))
        self.args.append(meta_func.meta_arg("team", "Team Id", "none"))

    def execute(self, args, server):
        key = args["key"]
        category = int(args["category"])
        rank = int(args["rank"])
        team = int(args["team"])

        if server.key == key:
            cat = server.game_data.get_category(category)

            if cat is not None:
                pool = []
                for q in cat.questions:
                    if q.rank == rank and not q.asked:
                        pool.append(q)

                if len(pool) > 0:
                    q_i = random.randint(0, len(pool)-1)
                    self.question = pool[q_i]
                    self.question.asked = True
                    self.points = server.game_data.points_table.points[self.question.rank]
                else:
                    raise func_error("No more question in this category with this rank")
            else:
                raise func_error("Invalid category")

        else:
            raise func_error("Invalid key")

    def answer(self):
        data = {'question': {
                    'id': self.question.id,
                    'question': self.question.question,
                    'answer': self.question.answer,
                    'rank': self.question.rank,
                    'points': self.points
                    }}

        return data

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


class get_all_teams(service_func):
    def __init__(self):
        service_func.__init__(self, "/team/all")
        self.name = "Get all teams"
        self.description = "Get all teams with id for current Jeopardy"
        self.teams = []

    def execute(self, args, server):
        self.teams = server.teams

    def answer(self):
        data = {"teams": []}
        for t in self.teams:
            data["teams"].append(t)

        return data


class add_team(service_func):
    def __init__(self):
        service_func.__init__(self, "/team/add")
        self.name = "Add team"
        self.description = "Add a new team to the jeopardy"
        self.args.append(meta_func.meta_arg("key", "Protection Key", "none"))
        self.args.append(meta_func.meta_arg("name", "New Team Name", "none"))
        self.team = None

    def execute(self, args, server):
        key = args["key"]
        name = args["name"]

        if key != server.key:
            raise func_error("Invalid key")
        else:
            max_id = 0
            for t in server.teams:
                if t[0] > max_id:
                    max_id = t[0]
                if t[1] == name:
                    raise func_error("Team name already exists")
            max_id += 1
            new_team = [max_id, name]
            server.teams.append(new_team)
            server.save_teams()
            self.team = new_team

    def answer(self):
        #returning new team id
        data = {"team_id": self.team[0]}
        return data