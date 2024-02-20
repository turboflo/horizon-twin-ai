from openai import OpenAI
from horizon_twin_ai.comparison import Comparison
from horizon_twin_ai.prompt import compare_project_prompt
import json


class GPTClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def compare_project(self, my_project: str, existing_project: str, model: str = "gpt-3.5-turbo") -> Comparison:
        prompt = compare_project_prompt(my_project, existing_project)
        completion = self.client.chat.completions.create(
            model=model,
            messages=prompt,
            response_format={"type": "json_object"},
        )
        content = completion.choices[0].message.content
        content_dict = json.loads(content)
        comparison = Comparison.from_dict(content_dict)
        return comparison
