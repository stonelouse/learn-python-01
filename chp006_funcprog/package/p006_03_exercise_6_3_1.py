def urlify(state):
    return "-".join(state.lower().split())

def states_to_url(states):
    return {state: urlify(state) for state in states}
