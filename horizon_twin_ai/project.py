
class Project:
    def __init__(self, id: str, score: float, values: list[float], title: str, objective: str):
        self.id = id
        self.score = score
        self.values = values
        self.title = title
        self.objective = objective

    def title_and_objective(self):
        return f"{self.title}\n{self.objective}"
