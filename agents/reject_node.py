def reject_node(state):
    """
    Called when user rejects a sensitive action.
    """

    print("\n[REJECT NODE]")

    state["answer"] = (
        "The requested operation was cancelled because approval was not granted."
    )

    return state