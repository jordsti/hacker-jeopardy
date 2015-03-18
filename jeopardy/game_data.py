__author__ = 'jguerin'

question_id = 0

def increment_question():
    global question_id
    id = question_id
    question_id += 1
    return id

category_id = 0

def increment_category():
    global category_id
    id = category_id
    category_id += 1
    return id

class points_table:
    def __init__(self, points=[200, 400, 600, 800, 1000]):
        self.points = points

    def count(self):
        return len(self.points)

class question:
    def __init__(self, question="", rank=0, answer=""):
        self.id = increment_question()
        self.question = question
        self.rank = rank
        self.answer = answer
        self.asked = False

class category:
    def __init__(self, name):
        self.id = increment_category()
        self.name = name
        self.questions = []

class game_data:
    def __init__(self):
        self.categories = []
        self.points_table = points_table()

    def get_category(self, cat_id):
        for cat in self.categories:
            if cat.id == cat_id:
                return cat

        return None

    def read_file(self, filepath):
        fp = open(filepath, 'r')
        lines = fp.readlines()
        fp.close()

        cat = None
        quest = None
        for l in lines:
            line = l.strip("\t").strip(" ").strip("\r").strip("\n")
            if line.startswith('category:'):
                cat = category(line[9:])
                self.categories.append(cat)
            elif line.startswith('question:'):
                quest = question()
                quest.question = line[9:]
                if cat is not None:
                    cat.questions.append(quest)
            elif line.startswith('rank:'):
                if quest is not None:
                    quest.rank = int(line[5:])
            elif line.startswith('answer:'):
                if quest is not None:
                    quest.answer = line[7:]
            elif line.startswith('points:'):
                points = line[7:]
                points = points.split(',')
                self.points_table.points = []
                for p in points:
                    self.points_table.points.append(int(p))
