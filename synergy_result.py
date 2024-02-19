from project import Project
from comparison import Comparison


class SynergyResult:
    def __init__(self, input: str, project: Project, comparison: Comparison):
        self.input = input
        self.project = project
        self.comparison = comparison

    def compact_strig(self) -> str:
        return f"GPT_SCORE={self.comparison.score} - PINECONE_SCORE:{self.project.score} - TITLE={self.project.title}"
