from agent.ai_agent import ask_llm, summarize
from client.mcp_client import MCPClient
from memory.conversation import ConversationMemory

memory = ConversationMemory()

async def process_question(question: str):

    memory.add_user(question)

    llm_response = ask_llm(memory.get_messages())

    if isinstance(llm_response, str):
        memory.add_assistant(llm_response)
        return llm_response

    tool_name = llm_response["tool"]
    arguments = llm_response["arguments"]

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