from datetime import datetime

from app.repositories.file_repository import FileRepository

from app.services.ai_service import AIService
from app.services.email_service import EmailService
from app.services.metrics_service import MetricsService

from app.utils.logger import logger


class ContactService:

    def __init__(self):

        self.repository = FileRepository()

        self.ai_service = AIService()
        self.email_service = EmailService()
        self.metrics_service = MetricsService()

    async def process_contact(self, request):

        ai_result = await self.ai_service.analyze_comment(
            request.comment
        )

        contact = {
            "name": request.name,
            "email": request.email,
            "phone": request.phone,
            "comment": request.comment,
            "created_at": datetime.utcnow().isoformat(),
            "ai": ai_result
        }

        try:

            self.repository.append_json(
                "contacts.json",
                contact
            )

            self.metrics_service.increment_success()

        except Exception:

            self.metrics_service.increment_failed()

            logger.exception(
                "Failed to save contact."
            )

            raise

        email_sent = self.email_service.send_contact_emails(
            contact
        )

        return {
            "success": True,
            "message": "Request accepted.",
            "email_sent": email_sent
        }