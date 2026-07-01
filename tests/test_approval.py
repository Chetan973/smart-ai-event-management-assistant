from pprint import pprint

from app.graph.nodes.approval import approval_node


state = {

    "customer_name": "Chetan P",

    "customer_email": "chetan@gmail.com",

    "customer_phone": "9876543210",

    "event_type": "Wedding",

    "event_date": "15 December",

    "venue": "Bangalore",

    "guest_count": 300,

    "food_preference": "Vegetarian",

}

response = approval_node(state)

print()

pprint(response)