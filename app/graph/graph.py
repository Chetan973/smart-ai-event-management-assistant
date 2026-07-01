"""
LangGraph Builder
"""

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from app.graph.approval_router import approval_router
from app.graph.entry_router import entry_router
from app.graph.state import EventState

from app.graph.router import router

from app.graph.nodes.planner import planner_node
from app.graph.nodes.booking import booking_node
from app.graph.nodes.conversation import conversation_node
#from app.checkpoint.postgres_checkpointer import checkpointer
from app.graph.nodes.approval import approval_node
from app.graph.nodes.faq import faq_node
from app.graph.nodes.payment import payment_node
from app.graph.conversation_router import conversation_router
from app.graph.nodes.save_booking import save_booking_node


builder = StateGraph(EventState)

# Nodes
builder.add_node("planner", planner_node)
builder.add_node("booking", booking_node)
builder.add_node("conversation", conversation_node)
builder.add_node(
    "approval",
    approval_node,
)
builder.add_node("faq", faq_node)
builder.add_node("payment", payment_node)
builder.add_node(
    "save_booking",
    save_booking_node,
)

# Start
builder.add_conditional_edges(
    START,
    entry_router,
    {
        "planner": "planner",
        "conversation": "conversation",
        "approval": "approval",
        "save_booking": "save_booking",
    },
)

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
builder.add_edge(
    "booking",
    "conversation",
)
builder.add_conditional_edges(
    "conversation",
    conversation_router,
    {
        "approval": "approval",
        "end": END,
    }
)

builder.add_edge("faq", END)

builder.add_conditional_edges(
    "approval",
    approval_router,
    {
        "save_booking": "save_booking",
        "end": END,
    },
)
builder.add_edge(
    "save_booking",
    "payment",
)
builder.add_edge("payment", END)
graph = builder.compile()