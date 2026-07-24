from pydantic import BaseModel


class ContactResponse(BaseModel):
    success: bool
    message: str