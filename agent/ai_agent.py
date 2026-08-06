import json
from openai import OpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_MODEL,
)

client = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=AZURE_OPENAI_ENDPOINT,
)

SYSTEM_PROMPT = """
You are an AI Agent.

You have the following tools available.

1. add(a,b)
Adds two numbers.

2. multiply(a,b)
Multiplies two numbers.

3. read_file(filename)
Reads a file from the data folder.

4. get_all_employees()
Returns all employees.

5. get_employee_by_id(id)
Returns a single employee by ID.

Always respond ONLY with JSON when a tool is required.

Examples:

User:
What is 25 + 75?

Response:
{
    "tool":"add",
    "arguments":{
        "a":25,
        "b":75
    }
}

User:
Multiply 20 and 30

Response:
{
    "tool":"multiply",
    "arguments":{
        "a":20,
        "b":30
    }
}

User:
Read employee.txt

Response:
{
    "tool":"read_file",
    "arguments":{
        "filename":"employee.txt"
    }
}

User:
Show all employees

Response:
{
    "tool":"get_all_employees",
    "arguments":{}
}

User:
Show employee with id 3

Response:
{
    "tool":"get_employee_by_id",
    "arguments":{
        "id":3
    }
}

If no tool is required, answer normally.
"""

def ask_llm(messages):
    print("Using Azure OpenAI")

    response = client.responses.create(
        model=AZURE_OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            *messages
        ]
    )
    content = response.output_text

    print("\n===== LLM Response =====\n")
    print(content)

    try:
        return json.loads(content)
    except Exception:
        return content

def summarize(question: str, tool_result):

    response = client.responses.create(
        model=AZURE_OPENAI_MODEL,
        input=[
            {
                "role": "system",
                "content": """
You are a helpful AI assistant.

Never mention:
- tools
- MCP
- databases
- SQL
- internal processing

Present results naturally.

If the result is a list, use bullet points or numbered lists.

Only use the supplied data.
Do not invent information.
""",
            },
            {
                "role": "user",
                "content": f"""
User Question:

{question}

Tool Result:

{tool_result}
""",
            },
        ],
    )

    return response.output_text

if __name__ == "__main__":

    result = ask_llm("What is 120 + 350 ?")

    print("\n===== Parsed =====\n")

    print(result)