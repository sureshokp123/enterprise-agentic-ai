# from langgraph.graph import StateGraph, END

# from agent.state import AgentState

# from agent.nodes import (
#     planner_node,
#     executor_node,
#     summarizer_node
# )

# graph = StateGraph(AgentState)

# graph.add_node("planner", planner_node)
# graph.add_node("executor", executor_node)
# graph.add_node("summarizer", summarizer_node)

# graph.set_entry_point("planner")


# def route(state):

#     if state.get("final_answer"):
#         return END

#     return "executor"


# graph.add_conditional_edges(
#     "planner",
#     route,
#     {
#         "executor": "executor",
#         END: END
#     }
# )

# graph.add_edge("executor", "summarizer")

# graph.add_edge("summarizer", END)

# agent_graph = graph.compile()

from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.supervisor import supervisor
from agents.rag_node import rag_node
from agents.tool_node import tool_node
from agents.llm_node import llm_node
from agents.approval_node import approval_node
from agents.reject_node import reject_node

class AgentState(TypedDict, total=False):
    question: str
    route: str
    context: str
    tool_result: str
    answer: str
    approved: bool
    approval_required: bool

def route_question(state: AgentState):

    route = state["route"]

    if route == "RAG":
        return "rag"

    if route == "TOOL":
        return "tool"

    return "approval"

# def route_after_approval(state):

#     if state["approved"]:
#         return "tool"

#     return "reject"

builder = StateGraph(AgentState)

builder.add_node("supervisor", supervisor)
builder.add_node("rag", rag_node)
builder.add_node("tool", tool_node)
builder.add_node("llm", llm_node)
builder.add_node("approval", approval_node)
builder.add_node("reject", reject_node)

builder.set_entry_point("supervisor")

builder.add_conditional_edges(
    "supervisor",
    route_question,
    {
        "rag": "rag",
        "tool": "tool",
        "approval": "approval",
    },
)

# builder.add_conditional_edges(
#     "approval",
#     route_after_approval,
#     {
#         "tool": "tool",
#         "reject": "reject",
#     },
# )

builder.add_edge("rag", "llm")
builder.add_edge("tool", "llm")
builder.add_edge("llm", END)
builder.add_edge("reject", END)
builder.add_edge("approval", END)

graph = builder.compile()

# if __name__ == "__main__":

#     result = graph.invoke(
#         {
#             "question": "Show all employees",
#         }
#     )

#     print("\nFinal State:\n")

#     print(result)

    # print("\n========== FINAL ANSWER ==========\n")

    # print(result["answer"])