from fastapi import APIRouter

from app.schemas.request import ContactRequest
from app.schemas.response import ContactResponse

from app.controllers.contact_controller import ContactController


router = APIRouter(
    prefix="/api",
    tags=["Contact"]
)

controller = ContactController()


@router.post(
    "/contact",
    response_model=ContactResponse,
    status_code=201
)
async def contact(
    request_data: ContactRequest
):

    return await controller.create(request_data)