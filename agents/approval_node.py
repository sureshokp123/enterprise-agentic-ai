# def approval_node(state):
#     """
#     Human-in-the-Loop Approval Node
#     """

#     question = state["question"]

#     print("\n========== APPROVAL REQUIRED ==========")
#     print(question)

#     choice = input("\nApprove this action? (yes/no): ").strip().lower()

#     if choice == "yes":
#         state["approved"] = True
#     else:
#         state["approved"] = False

#     return state

def approval_node(state):

    if "approved" not in state:
        state["approval_required"] = True
        return state

    if not state["approved"]:
        state["answer"] = "Request Rejected."
        state["approval_required"] = False
        return state

    state["approval_required"] = False

    return state