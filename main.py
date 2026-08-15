from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from agent.graph import graph
from agents.tool_node import tool_node
from agents.llm_node import llm_node
from database.seed_employees import seed_employees

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

# seed_employees()  # Seed the database with initial employees

@app.post("/chat")
def chat(request: ChatRequest):

    state = {
        "question": request.question
    }

    result = graph.invoke(state)

    # Human approval required
    if result.get("approval_required"):

        return {
            "approval": True,
            "state": result
        }

    return {
        "approval": False,
        "answer": result.get("answer")
    }

class ApprovalRequest(BaseModel):
    state: dict
    approved: bool


@app.post("/approve")
def approve(request: ApprovalRequest):

    state = request.state

    # User rejected
    if not request.approved:

        return {
            "answer": "Operation Cancelled."
        }

    # Continue execution

    state["approved"] = True

    state = tool_node(state)

    state = llm_node(state)

    return {
        "answer": state["answer"]
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "enterprise-agentic-ai"
    }