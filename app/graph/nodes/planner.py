"""
Planner Node
"""

from app.graph.state import EventState
from app.prompts.planner_prompt import PLANNER_PROMPT
from app.services.gemini_service import GeminiService

gemini = GeminiService()


def planner_node(state: EventState) -> EventState:

    prompt = f"""
{PLANNER_PROMPT}

User:

{state["user_input"]}
"""

    result = gemini.generate_json(prompt)

    state["intent"] = result.get("intent", "")

    state["event_type"] = result.get("event_type", "")

    state["guest_count"] = result.get("guest_count", 0)

    state["event_date"] = result.get("event_date", "")

    state["venue"] = result.get("venue", "")

    state["food_preference"] = result.get("food_preference", "")

    state["customer_name"] = result.get("customer_name", "")

    state["customer_email"] = result.get("customer_email", "")

    state["customer_phone"] = result.get("customer_phone", "")

    state["missing_fields"] = result.get("missing_fields", [])

    state["planner_response"] = result

    return state