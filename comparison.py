from typing import Any


class Comparison:
    def __init__(self, summary, similarity, difference, score, reason):
        self.summary = summary
        self.similarity = similarity
        self.difference = difference
        self.score = score
        self.reason = reason

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        summary = data['Summary']
        similarity = data['Similarity']
        difference = data['Difference']
        score = data['Score']
        reason = data['Reason']
        return cls(summary, similarity, difference, score, reason)
