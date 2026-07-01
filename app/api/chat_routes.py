"""
Chat API

Entry point for AI conversation.
"""

from fastapi import APIRouter

from app.graph.graph import graph

from app.api.schemas import ChatRequest
from app.api.schemas import ChatResponse

from app.memory.session_manager import (
    get_state,
    save_state,
)

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)


@router.post(
    "/{session_id}",
    response_model=ChatResponse,
)
def chat(
    session_id: str,
    request: ChatRequest,
):

    # ----------------------------------
    # Load Previous Conversation
    # ----------------------------------

    state = get_state(session_id)

    # ----------------------------------
    # Update User Message
    # ----------------------------------

    state["user_input"] = request.message

    # ----------------------------------
    # Execute LangGraph
    # ----------------------------------

    result = graph.invoke(state)

    # ----------------------------------
    # Save Updated State
    # ----------------------------------

    save_state(
        session_id,
        result,
    )

    # ----------------------------------
    # Return Response
    # ----------------------------------

    return ChatResponse(

        reply=result["final_response"],

        intent=result["intent"],

    )