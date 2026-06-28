from pydantic import BaseModel, EmailStr


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