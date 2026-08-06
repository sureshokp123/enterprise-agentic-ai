from fastapi import FastAPI
from pydantic import BaseModel

from services.agent_service import process_question

app = FastAPI(
    title="MCP AI Agent",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    answer = await process_question(request.message)

    return ChatResponse(answer=str(answer))