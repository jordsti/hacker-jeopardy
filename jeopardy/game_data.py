
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

team_id = 0

def increment_team():
    global team_id
    id = team_id
    team_id += 1
    return id


class points_table:
    def __init__(self, points=[200, 400, 600, 800, 1000]):
        self.points = points

    def count(self):
        return len(self.points)

class team:
    def __init__(self, name):
        self.id = increment_team()
        self.name = name
        self.points = 0

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
        self.ranks_available = []

class game_data:
    (TeamsCount) = (4)
    def __init__(self):
        self.categories = []
        self.points_table = points_table()
        self.current_question = None
        self.teams = []
        self.game_on = False

    def start_game(self):

        if not self.game_on:
            # checking if the numbers of team is ok
            if len(self.teams) == self.TeamsCount:
                print "Starting the game !"
                self.game_on = True
            else:
                print "Only %d teams are registered..." % (len(self.teams))
        else:
            print "Game is already started!"

    def get_team(self, team_id):
        for t in self.teams:
            if t.id == team_id:
                return t

        return None

    def new_team(self, team_name):
        t = team(team_name)
        self.teams.append(t)
        return t

    def ask_question(self, question, team):
        self.current_question = question_context(question, team, self.points_table.points[question.rank])

    def valid_answer(self):
        if self.current_question is not None:
            _team = self.get_team(self.current_question.team)
            if _team is not None:
                _team.points += self.current_question.points
                self.current_question = None

    def get_category(self, cat_id):
        for cat in self.categories:
            if cat.id == cat_id:
                return cat

        return None

    def fill_rank_available(self):
        for c in self.categories:
            for i in range(len(self.points_table.points)):
                c.ranks_available.append(True)

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

        self.fill_rank_available()

class question_context:
    def __init__(self, question, team, points):
        self.question = question
        self.team = team
        self.points = points