from pydantic import BaseModel, EmailStr, Field, field_validator
import re

PHONE_REGEX = re.compile(r"^\+?[0-9\-()\s]{10,20}$")


class ContactRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str
    comment: str = Field(..., min_length=5, max_length=3000)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if not PHONE_REGEX.match(value):
            raise ValueError("Invalid phone number")
        return value