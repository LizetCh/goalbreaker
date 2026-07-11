
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# pydantic model for the request body


class QueryRequest(BaseModel):
    prompt: str


@app.post("/ask")
async def ask_llm(request: QueryRequest):
    return {"status": "success", "response": f"Recibí tu prompt: {request.prompt}"}
