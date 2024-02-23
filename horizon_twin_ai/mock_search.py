from horizon_twin_ai.result import Result
from horizon_twin_ai.project import Project
from horizon_twin_ai.comparison import Comparison
import random


def mock_search_and_compare(project_description: str, top_k: int = 5) -> list[Result]:
    results = []
    for _ in range(top_k):
        project = Project(
            id="mock_project_id",
            score=random.uniform(0.5, 1.0),  # Random score between 0.5 and 1.0
            values=None,
            title="Mock Project Title",
            objective="This is a mock project description. It aims to demonstrate a generic approach to integrating renewable energy solutions in rural areas, focusing on sustainability, regional development, and optimizing the use of local resources.",
        )

        comparison = Comparison(
            summary="This mock comparison summarizes the alignment between your project idea and the mock project, focusing on renewable energy and sustainability in rural areas.",
            similarity="Both your project and the mock project aim to enhance renewable energy use and support rural communities, though with different specific focuses.",
            difference="While the mock project emphasizes biogas and biomass, your project may focus on other renewable sources or aspects of rural development.",
            # Random similarity score between 60 and 100
            score=random.randint(50, 100),
            reason="The similarity and difference in focus result in a randomly assigned score reflecting the conceptual alignment between the projects.",
        )

        mock_result = Result(
            input=project_description,
            project=project,
            comparison=comparison,
        )

        results.append(mock_result)

    # Sort the results by comparison.score in descending order
    sorted_results = sorted(results, key=lambda x: x.comparison.score, reverse=True)

    return sorted_results
