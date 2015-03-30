from ..service_func import service_func, meta_arg, func_error


class current_question(service_func):
    def __init__(self):
        service_func.__init__(self, "/question/current")
        self.name = "Get the current question"
        self.description = "Return the current question or nothing if there is ongoing question"
        self.args.append(meta_arg("key", "Protection key", "none"))
        self.question = None

    def init(self):
        self.question = None

    def execute(self, args, server):
        self.check_server_key(args, server)

        if server.game_data.current_question is not None:
            self.question = server.game_data.current_question

    def answer(self):
        data = {}
        if self.question is not None:
            data["question"] = {
                "question": self.question.question.question,
                "answer": self.question.question.answer,
                "team": self.question.team,
                "points": self.question.points
            }

        return data