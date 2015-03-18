#this will answer the current answer in game_data.current_question
from ..service_func import service_func, meta_arg, func_error


class answer_question(service_func):

    def __init__(self):
        service_func.__init__(self, "/question/answer")
        self.name = "Answer question"
        self.description = "Answer the current question"
        self.args.append(meta_arg("key", "Protection key", "none"))
        self.args.append(meta_arg("valid", "Is the answer is good or not (true or false)", "none"))
        self.args.append(meta_arg("next_team", "If the answer is invalid, next team to got a chance to answer, if it -1, the question is removed from current_question", "none"))

    def execute(self, args, server):
        key = args["key"]
        valid = bool(args["valid"])

        if server.key == key:
            if server.game_data.current_question is not None:
                if valid:
                    server.game_data.valid_answer()
                else:
                    next_team = int(args["next_team"])

                    if next_team == -1:
                        # question is ended, nobody gets the points
                        server.game_data.current_question = None
                    else:
                        # this team got a chance to answer this question
                        server.game_data.current_question.team = next_team
            else:
                raise func_error("No question waiting for an answer")
        else:
            raise func_error("Invalid key")

    def answer(self):
        # nothing to send here
        return {}