from pprint import pprint

from app.graph.graph import graph

state = {
    "user_input":
    """
I want to organize a wedding for 300 guests
on 15 December in Bangalore.
"""
}

response = graph.invoke(state)

pprint(response)