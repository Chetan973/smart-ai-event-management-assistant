from fastapi import APIRouter

from app.api.chat_routes import router as chat_router

router = APIRouter()

router.include_router(chat_router)


# router.include_router(booking_router)

# router.include_router(payment_router)

# router.include_router(email_router)


@router.get("/health")
def health():
    return {
        "status": "UP",
        "service": "Smart AI Event Management Assistant"
    }