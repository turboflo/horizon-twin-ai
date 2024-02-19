
class Project:
    def __init__(self, id, score, values, title, objective):
        self.id = id
        self.score = score
        self.values = values
        self.title = title
        self.objective = objective

    def title_and_objective(self):
        return f"{self.title}\n{self.objective}"