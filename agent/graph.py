from langgraph.graph import StateGraph, END

from agent.state import AgentState

from agent.nodes import (
    planner_node,
    executor_node,
    summarizer_node
)

graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("executor", executor_node)
graph.add_node("summarizer", summarizer_node)

graph.set_entry_point("planner")


def route(state):

    if state.get("final_answer"):
        return END

    return "executor"


graph.add_conditional_edges(
    "planner",
    route,
    {
        "executor": "executor",
        END: END
    }
)

graph.add_edge("executor", "summarizer")

graph.add_edge("summarizer", END)

agent_graph = graph.compile()