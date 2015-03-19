__author__ = 'jguerin'
import threading
import BaseHTTPServer
import handler
import service_func
import os
import pickle
import funcs

class HttpServer(BaseHTTPServer.HTTPServer):

    def __init__(self, addr, handler):
        self.key = "hacker"
        self.files_dir = "./"
        self.functions = []
        BaseHTTPServer.HTTPServer.__init__(self, addr, handler)

        self.service_func = service_func.default_func([])
        self.functions.append(self.service_func)
        self.functions.append(funcs.test_key())

        # teams functions
        self.functions.append(funcs.add_team())
        self.functions.append(funcs.get_all_teams())
        self.functions.append(funcs.remove_team())

        # categories
        self.functions.append(funcs.get_all_categories())
        self.functions.append(funcs.get_points_table())
        self.functions.append(funcs.get_categories_rank())

        # questions
        self.functions.append(funcs.ask_question())
        self.functions.append(funcs.answer_question())


        self.service_func.functions = self.functions
        self.teams = []
        self.game_data = None

    def get_teams_file(self):
        return os.path.join(self.files_dir, "teams.pickle")

    def load_teams(self):
        if os.path.exists(self.get_teams_file()):
            fp = open(self.get_teams_file(), 'r')
            self.teams = pickle.load(fp)
            fp.close()
        else:
            print "No team found !"

    def save_teams(self):
        fp = open(self.get_teams_file(), 'w')
        pickle.dump(self.teams, fp)
        fp.close()


class service_thread(threading.Thread):
    def __init__(self, listen_port=8080):
        threading.Thread.__init__(self)
        self.port = listen_port
        self.handler = None
        self.httpd = None
        self.handler = handler.service_handler
        self.httpd = HttpServer(("", self.port), self.handler)
        self.httpd.load_teams()

    def run(self):
        print "Starting the Web Service on port %d" % self.port
        self.httpd.serve_forever()





