from openai import OpenAI
from comparison import Comparison
from prompt import compare_project_prompt
import json


class GPTClient:
    def __init__(self, api_key: str, model_name: str = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def compare_project(self, my_project: str, existing_project: str) -> Comparison:
        prompt = compare_project_prompt(my_project, existing_project)
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=prompt
        )
        content = completion.choices[0].message.content
        content_dict = json.loads(content)
        comparison = Comparison.from_dict(content_dict)
        return comparison
