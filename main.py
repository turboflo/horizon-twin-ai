from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from horizon_twin_ai.mock_search import mock_search_and_compare
from horizon_twin_ai.client import Client

import os

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

app = FastAPI()
client = Client(pinecone_api_key=PINECONE_API_KEY, openai_api_key=OPENAI_API_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


class QueryPayload(BaseModel):
    project_description: str
    model: str = "gpt-3.5-turbo"
    top_k: int = Field(3, gt=0, lt=11)  # greater than 0 and less than 11


@app.post("/query")
async def query(payload: QueryPayload):
    # results = mock_search_and_compare(
    #     project_description=payload.project_description, top_k=payload.top_k
    # )
    results = client.search_and_compare(
        project_description=payload.project_description,
        model=payload.model,
        top_k=payload.top_k,
    )
    response = {
        "project_description": payload.project_description,
        "model": payload.model,
        "top_k": payload.top_k,
        "results": results,
    }
    return response
