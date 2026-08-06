from langgraph.graph import StateGraph, END

from agent.state import AgentState
from agent.nodes import planner_node

graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)

graph.set_entry_point("planner")

graph.add_edge("planner", END)

agent_graph = graph.compile()