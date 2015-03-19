from ..service_func import service_func, func_error, meta_arg


class test_key(service_func):
    def __init__(self):
        service_func.__init__(self, "/key")
        self.name = "Test Key"
        self.description = "Test the protection key if it's valid or not"
        self.args.append(meta_arg("key", "Protection key", "none"))
        self.valid = False

    def init(self):
        self.valid = False

    def execute(self, args, server):
        key = args["key"]
        self.valid = key == server.key

    def answer(self):
        data = {"valid": self.valid}
        return data