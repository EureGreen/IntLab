import json

from openai import OpenAI

from app.config import settings
from app.utils.logger import logger


class AIService:

    def __init__(self):

        self.client = None

        if settings.OPENROUTER_API_KEY:

            self.client = OpenAI(
                api_key=settings.OPENROUTER_API_KEY,
                base_url=settings.OPENROUTER_BASE_URL
            )

    async def analyze_comment(
        self,
        comment: str
    ) -> dict:
        """
        Анализирует комментарий пользователя.

        При любой ошибке возвращает fallback.
        """

        if self.client is None:

            logger.warning(
                "OpenRouter API key not configured."
            )

            return self._fallback()

        try:

            response = self.client.chat.completions.create(

                model=settings.OPENROUTER_MODEL,

                temperature=0,

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Ты анализируешь обращения клиентов. "
                            "Верни ТОЛЬКО JSON без пояснений.\n\n"
                            "{"
                            "\"sentiment\":\"positive|neutral|negative\","
                            "\"category\":\"...\","
                            "\"summary\":\"...\""
                            "}"
                        )
                    },
                    {
                        "role": "user",
                        "content": comment
                    }
                ]
            )

            content = response.choices[0].message.content

            logger.info(
                "AI response: %s",
                content
            )

            return json.loads(content)

        except Exception as ex:

            logger.exception(
                "AI error: %s",
                ex
            )

            return self._fallback()

    def _fallback(self):

        return {
            "sentiment": "unknown",
            "category": "unknown",
            "summary": "AI unavailable"
        }