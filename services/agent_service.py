from agent.graph import agent_graph
from memory.conversation import ConversationMemory

memory = ConversationMemory()


async def process_question(question: str):

    memory.add_user(question)

    state = {
        "question": question,
        "llm_response": None,
        "tool_name": "",
        "tool_args": {},
        "tool_result": None,
        "final_answer": ""
    }

    result = await agent_graph.ainvoke(state)

    answer = result["final_answer"]

    memory.add_assistant(answer)

    return answer