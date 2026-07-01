"""
Test Update State Node
"""

from pprint import pprint

from app.graph.nodes.update_state import update_state_node


state = {
    "current_field": "food_preference",
    "user_input": "Vegetarian",
    "missing_fields": [
        "food_preference",
        "customer_name",
        "customer_email",
    ],
}

response = update_state_node(state)

print("\nUpdate State Output\n")

pprint(response)