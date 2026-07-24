from app.services.contact_service import ContactService


class ContactController:

    def __init__(self):
        self.service = ContactService()

    async def create(self, request_data):

        return await self.service.process_contact(
            request_data
        )