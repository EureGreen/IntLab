from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Backend AI Contact API"

    APP_ENV: str = "development"

    APP_HOST: str = "0.0.0.0"

    APP_PORT: int = 8000


    # ---------- OpenRouter ----------

    OPENROUTER_API_KEY: str = ""

    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    OPENROUTER_MODEL: str = "qwen/qwen3-8b:free"


    # ---------- SMTP ----------

    SMTP_HOST: str = ""

    SMTP_PORT: int = 587

    SMTP_USERNAME: str = ""

    SMTP_PASSWORD: str = ""

    OWNER_EMAIL: str = ""


    # ---------- Rate limit ----------

    RATE_LIMIT_REQUESTS: int = 5

    RATE_LIMIT_WINDOW: int = 60


    # ---------- Logging ----------

    LOG_FILE: str = "data/logs/app.log"


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()