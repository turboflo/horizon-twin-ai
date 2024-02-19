from pinecone_client import PineconeClient
from gpt_client import GPTClient
from synergy_result import SynergyResult


class HorizonSynergyAI():
    def __init__(self, pinecone_api_key: str, openai_api_key: str):
        self.pinecone = PineconeClient(api_key=pinecone_api_key)
        self.gpt = GPTClient(api_key=openai_api_key)

    def search_and_compare(self, project_description: str, top_k: int = 5,
                           model: str = "gpt-3.5-turbo") -> list[SynergyResult]:
        results = []
        projects = self.pinecone.search(query=project_description, top_k=top_k)
        for project in projects:
            comparison = self.gpt.compare_project(
                my_project=project_description,
                existing_project=project.title_and_objective(),
                model=model,
                )
            results.append(SynergyResult(input=project_description, project=project, comparison=comparison))
        return results
