"""
Test Conversation Node
"""

from pprint import pprint

from app.graph.nodes.conversation import conversation_node


state = {
    "missing_fields": [
        "food_preference",
        "customer_name",
        "customer_email",
        "customer_phone",
    ]
}

response = conversation_node(state)

print("\nConversation Node Output\n")

pprint(response)