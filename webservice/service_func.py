__author__ = 'jguerin'
from meta_func import meta_func, meta_arg

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

    def init(self):
        pass

    def execute(self, args, server):
        pass

    def answer(self):
        pass

    def get_meta(self):
        meta = meta_func(self.func_path)
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
        return {'functions': metas, 'version': 1}








