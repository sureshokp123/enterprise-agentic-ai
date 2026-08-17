import asyncio
import re

from client.mcp_client import MCPClient


def tool_node(state):
    """
    LangGraph Tool Node
    """

    question = state["question"].lower()

    print("\n[TOOL NODE]")
    print(f"Question : {question}")

    client = MCPClient()

    # -----------------------------
    # Show all employees
    # -----------------------------
    if "all employees" in question:

        # print("\n[TOOL NODE]")
        # print("Question :", question)
        
        result = asyncio.run(
            client.call_tool(
                "get_all_employees",
                {}
            )
        )

        # print("\n[MCP TOOL RESULT]")
        # print(result)
        # print("====================")

    # -----------------------------
    # Delete employee
    # -----------------------------
    elif "delete employee" in question:

        match = re.search(r"\d+", question)

        if not match:
            state["tool_result"] = "Employee ID not provided."
            return state

        employee_id = int(match.group())

        result = asyncio.run(
            client.call_tool(
                "delete_employee",
                {
                    "employee_id": employee_id
                }
            )
        )

    
    # -----------------------------
    # Update employee by ID
    # -----------------------------

    elif "update employee" in question:

        numbers = re.findall(r"\d+", question)

        if len(numbers) == 0:
            state["tool_result"] = "Employee ID missing."
            return state

        employee_id = int(numbers[0])

        field = None

        if "salary" in question:
            field = "salary"

        elif "department" in question:
            field = "department"

        elif "name" in question:
            field = "name"

        else:
            state["tool_result"] = "No valid field found."
            return state

        value = question.split("to")[-1].strip()

        result = asyncio.run(
            client.call_tool(
                "update_employee",
                {
                    "employee_id": employee_id,
                    "field": field,
                    "value": value
                }
            )
        )

    # -----------------------------
    # Add employee
    # -----------------------------
    elif "add employee" in question:

        data = question.replace("add employee", "").strip()

        parts = data.split()

        if len(parts) < 3:
            state["tool_result"] = (
                "Usage: Add employee <name> <department> <salary>"
            )
            return state

        name = parts[0]
        department = parts[1]
        salary = int(parts[2])

        result = asyncio.run(
            client.call_tool(
                "add_employee",
                {
                    "name": name,
                    "department": department,
                    "salary": salary,
                },
            )
    )

    # -----------------------------
    # Get employee by ID
    # -----------------------------
    elif "employee" in question and "delete" not in question and "update" not in question and "add" not in question:

        match = re.search(r"\d+", question)

        if not match:
            state["tool_result"] = "Employee ID not provided."
            return state

        employee_id = int(match.group())

        result = asyncio.run(
            client.call_tool(
                "get_employee_by_id",
                {
                    "id": employee_id
                }
            )
        )

    else:

        state["tool_result"] = "No matching tool found."

        return state

    tool_output = "\n".join([item.text for item in result.content])

    state["tool_result"] = tool_output

    return state


if __name__ == "__main__":

    state = {
        "question": "Show all employees"
    }

    result = tool_node(state)

    print("\n===== RAW MCP RESULT =====")

    print(result)

    tool_output = "\n".join(item.text for item in result.content)

    print("\n===== TOOL OUTPUT =====")
    print(tool_output)

    state["tool_result"] = tool_output