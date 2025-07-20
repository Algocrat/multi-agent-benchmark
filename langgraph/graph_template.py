from langgraph.graph import StateGraph, END
from typing import TypedDict, List

def create_graph(llm):
    def planner(state):
        return {
            'sections': [
                "Impact of AI on white-collar jobs",
                "Future of remote work with AI",
                "AI and automation in blue-collar sectors",
                "Policy & ethical challenges"
            ],
            'current_index': 0,
            'outputs': []
        }

    def researcher(state):
        section = state['sections'][state['current_index']]
        response = llm.invoke(f"Write a 300-word analysis on: {section}")
        return {
            'outputs': state['outputs'] + [response.content],
            'current_index': state['current_index'] + 1,
            'sections': state['sections']
        }

    def composer(state):
        return {
            'final_report': "\n\n".join(state.get('outputs', []))
        }

    class GraphState(TypedDict):
        sections: List[str]
        outputs: List[str]
        current_index: int
        final_report: str

    builder = StateGraph(GraphState)

    builder.add_node("planner", planner)
    builder.add_conditional_edges("planner", lambda s: "researcher")

    def route(state):
        if state["current_index"] < len(state["sections"]):
            return "researcher"
        else:
            return "composer"

    builder.add_node("researcher", researcher)
    builder.add_node("composer", composer)

    builder.add_conditional_edges("researcher", route)
    builder.add_edge("composer", END)

    builder.set_entry_point("planner")

    return builder.compile()

