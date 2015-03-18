from ..service_func import service_func, func_error, meta_arg
import random

class ask_question(service_func):
    def __init__(self):
        service_func.__init__(self, '/question/ask')
        self.name = "Ask Question"
        self.description = "Ask a question to a team, with a category id and a rank"
        self.question = None
        self.points = 0
        self.args.append(meta_arg("key", "Protection Key", "none"))
        self.args.append(meta_arg("category", "Category Id", "none"))
        self.args.append(meta_arg("rank", "Rank Id", "none"))
        self.args.append(meta_arg("team", "Team Id", "none"))

    def init(self):
        self.question = None
        self.points = 0

    def execute(self, args, server):
        key = args["key"]
        category = int(args["category"])
        rank = int(args["rank"])
        team = int(args["team"])

        if server.key == key:
            cat = server.game_data.get_category(category)

            if cat is not None:
                if cat.ranks_available[rank]:
                    if server.game_data.current_question is None:
                        pool = []
                        for q in cat.questions:
                            if q.rank == rank and not q.asked:
                                pool.append(q)

                        if len(pool) > 0:
                            q_i = random.randint(0, len(pool)-1)
                            self.question = pool[q_i]
                            self.question.asked = True
                            self.points = server.game_data.points_table.points[self.question.rank]
                            server.game_data.ask_question(self.question, team)
                            cat.ranks_available[rank] = False
                        else:
                            raise func_error("No more question in this category with this rank")
                    else:
                        raise func_error("A question is already asked and waiting for an answer")
                else:
                    raise func_error("You can't ask anymore question with this rank and category")
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

