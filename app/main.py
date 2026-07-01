from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Smart AI Event Management Assistant",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Smart AI Event Management Assistant API"
    }