__author__ = 'jguerin'

import json

class meta_arg:
    def __init__(self, name, description, default):
        self.name = name
        self.description = description
        self.default = default

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'default': self.default
        }

class meta_func:
    def __init__(self, func_path):
        self.func_path = func_path
        self.name = ""
        self.description = ""
        self.args = []

    def to_dict(self):

        args = []
        for a in self.args:
            args.append(a.to_dict())

        return {
            'name': self.name,
            'path': self.func_path,
            'description': self.description,
            'args': args
        }
