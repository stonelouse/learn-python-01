def functional_urls(states):
    return ["-".join(state.lower().split()) for state in states]
