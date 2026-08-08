from typing import TypedDict


class AgentState(TypedDict, total=False):
    question: str

    # Supervisor
    route: str

    # RAG
    context: str

    # MCP
    tool_name: str
    tool_args: dict
    tool_result: str

    # LLM
    answer: str
    
    approved: bool
    approval_required: bool