from pydantic import BaseModel, EmailStr

from decimal import Decimal


class CustomerCreateRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str


class CustomerResponse(BaseModel):
    customer_id: int
    full_name: str
    email: EmailStr
    phone_number: str

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):

    customer_id: int

    event_name: str

    event_type: str

    event_date: str

    guest_count: int

    venue_name: str

    venue_address: str

    food_preference: str

    decoration_theme: str

    estimated_budget: Decimal

    special_requirements: str | None = None


class BookingResponse(BaseModel):

    booking_id: int

    booking_status: str

    message: str

    class Config:
        from_attributes = True


class ChatRequest(BaseModel):

    message: str


class ChatResponse(BaseModel):

    reply: str

    intent: str