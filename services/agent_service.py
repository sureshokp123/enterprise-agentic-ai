from agent.ai_agent import summarize
from agent.graph import agent_graph
from client.mcp_client import MCPClient
from memory.conversation import ConversationMemory

memory = ConversationMemory()


async def process_question(question: str):

    memory.add_user(question)

    # LangGraph Planner
    state = agent_graph.invoke(
        {
            "question": question,
            "llm_response": None,
            "tool_name": "",
            "tool_args": {},
            "tool_result": None,
            "final_answer": "",
        }
    )

    # If planner answered directly
    if state.get("final_answer"):
        memory.add_assistant(state["final_answer"])
        return state["final_answer"]

    tool_name = state["tool_name"]
    arguments = state["tool_args"]

    client = MCPClient()

    result = await client.call_tool(
        tool_name,
        arguments
    )

    if result.structured_content:
        tool_result = result.structured_content["result"]
    else:
        tool_result = str(result)

    answer = summarize(question, tool_result)

    memory.add_assistant(answer)

    return answer