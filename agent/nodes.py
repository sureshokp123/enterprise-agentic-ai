from agent.agent import ask_llm


def planner_node(state):
    """
    Planner Agent

    Decides which tool should execute.
    """

    question = state["question"]

    response = ask_llm(
        [
            {
                "role": "user",
                "content": question,
            }
        ]
    )

    if isinstance(response, dict):
        state["tool_name"] = response.get("tool")
        state["tool_args"] = response.get("arguments", {})
    else:
        state["final_answer"] = response

    state["llm_response"] = response

    return state