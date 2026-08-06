from typing import TypedDict

class AgentState(TypedDict):
    question: str
    llm_response: str
    agent: str
    tool_name: str
    tool_args: dict
    tool_result: str
    final_answer: str