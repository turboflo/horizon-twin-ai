
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from project import Project


class PineconeClient:
    def __init__(self, api_key, index_name="horizon-projects", model_name="sentence-transformers/all-mpnet-base-v2"):
        pc = Pinecone(api_key=api_key)
        self.index = pc.Index(index_name)
        self.model = SentenceTransformer(model_name)

    def search(self, query, top_k=5, include_values=True, include_metadata=True) -> list[Project]:
        vectors = self.model.encode([query])
        vector = vectors[0].tolist()
        results = self.index.query(vector=vector,
                                   top_k=top_k,
                                   include_values=include_values,
                                   include_metadata=include_metadata)
        projects = []

        for match in results.to_dict().get('matches', []):
            id = match.get('id')
            score = match.get('score')
            values = match.get('values')
            title = match.get('metadata', {}).get('title')
            objective = match.get('metadata', {}).get('objective')
            project = Project(id, score, values, title, objective)
            projects.append(project)

        return projects
