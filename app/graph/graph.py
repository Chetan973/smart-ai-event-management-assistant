"""
LangGraph Builder
"""

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from app.graph.state import EventState

from app.graph.router import router

from app.graph.nodes.planner import planner_node
from app.graph.nodes.booking import booking_node
from app.graph.nodes.faq import faq_node
from app.graph.nodes.payment import payment_node


builder = StateGraph(EventState)

# Nodes
builder.add_node("planner", planner_node)
builder.add_node("booking", booking_node)
builder.add_node("faq", faq_node)
builder.add_node("payment", payment_node)

# Start
builder.add_edge(START, "planner")

# Conditional Routing
builder.add_conditional_edges(
    "planner",
    router,
    {
        "booking": "booking",
        "faq": "faq",
        "payment": "payment",
        "planner": END,
    },
)

# End
builder.add_edge("booking", END)
builder.add_edge("faq", END)
builder.add_edge("payment", END)

graph = builder.compile()