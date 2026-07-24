import smtplib
from email.message import EmailMessage

from app.config import settings
from app.utils.logger import logger


class EmailService:

    def send_contact_emails(self, contact: dict) -> bool:
        """
        Отправляет письмо владельцу и копию пользователю.

        Возвращает:
            True - если оба письма успешно отправлены
            False - если произошла ошибка
        """

        try:
            with smtplib.SMTP(
                settings.SMTP_HOST,
                settings.SMTP_PORT,
                timeout=15
            ) as smtp:

                smtp.starttls()

                smtp.login(
                    settings.SMTP_USERNAME,
                    settings.SMTP_PASSWORD
                )

                smtp.send_message(
                    self._owner_message(contact)
                )

                smtp.send_message(
                    self._user_message(contact)
                )

            return True

        except Exception as ex:

            logger.exception(
                f"SMTP error: {ex}"
            )

            return False

    def _owner_message(
        self,
        contact: dict
    ) -> EmailMessage:

        ai = contact.get("ai", {})

        msg = EmailMessage()

        msg["Subject"] = "Новое обращение"

        msg["From"] = settings.SMTP_USERNAME

        msg["To"] = settings.OWNER_EMAIL

        msg.set_content(
            f"""
Новое обращение

Имя: {contact['name']}
Email: {contact['email']}
Телефон: {contact['phone']}

Комментарий

{contact['comment']}

========================

AI

Настроение:
{ai.get("sentiment")}

Категория:
{ai.get("category")}

Резюме:
{ai.get("summary")}
"""
        )

        return msg

    def _user_message(
        self,
        contact: dict
    ) -> EmailMessage:

        msg = EmailMessage()

        msg["Subject"] = "Спасибо за обращение"

        msg["From"] = settings.SMTP_USERNAME

        msg["To"] = contact["email"]

        msg.set_content(
            f"""
Здравствуйте, {contact['name']}!

Спасибо за обращение.

Мы получили вашу заявку.

Наш специалист свяжется с вами в ближайшее время.
"""
        )

        return msg