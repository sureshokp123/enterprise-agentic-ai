from agent.ai_agent import ask_llm, summarize
from client.mcp_client import MCPClient


def planner_node(state):

    question = state["question"]

    response = ask_llm(
        [
            {
                "role": "user",
                "content": question
            }
        ]
    )

    state["llm_response"] = response

    if isinstance(response, dict):

        state["tool_name"] = response["tool"]
        state["tool_args"] = response["arguments"]

    else:

        state["final_answer"] = response

    print("PLANNER", state)

    return state


async def executor_node(state):

    print(f"Executing Tool : {state['tool_name']}")

    client = MCPClient()

    result = await client.call_tool(
        state["tool_name"],
        state["tool_args"]
    )

    if result.structured_content:
        state["tool_result"] = result.structured_content["result"]
    else:
        state["tool_result"] = str(result)

    print("EXECUTOR", state)
    return state


def summarizer_node(state):

    answer = summarize(
        state["question"],
        state["tool_result"]
    )

    state["final_answer"] = answer

    print("SUMMARIZER", state)
    return state