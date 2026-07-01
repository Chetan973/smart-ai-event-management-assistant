from pprint import pprint

from app.graph.graph import graph


config = {
    "configurable": {
        "thread_id": "user-001"
    }
}


state = {

    "user_input":
    "I want a wedding for 300 guests in Bangalore on 15 December."

}


response = graph.invoke(
    state,
    config=config
)

print()

pprint(response)