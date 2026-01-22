import json
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_PROJECT_NAME = "Skill Chatbot API"
DEFAULT_API_V1_PREFIX = "/api/v1"
DEFAULT_PROVIDERS_JSON = json.dumps(
    [
        {
            "host": "openai",
            "base_url": "https://api.openai.com/v1",
            "api_key_env": "OPENAI_API_KEY",
            "models": [{"id": "gpt-5.2-2025-12-11", "name": "GPT-5.2"}],
        },
        {
            "host": "minimax",
            "base_url": "https://api.minimaxi.com/v1",
            "api_key_env": "MINIMAX_API_KEY",
            "models": [
                {"id": "MiniMax-M2.1-lightning", "name": "MiniMax M2.1 Lightning"},
                {"id": "MiniMax-M2.1", "name": "MiniMax M2.1"},
                {"id": "MiniMax-M2", "name": "MiniMax M2"},
            ],
        },
    ],
    ensure_ascii=True,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    PROJECT_NAME: str = DEFAULT_PROJECT_NAME
    API_V1_PREFIX: str = DEFAULT_API_V1_PREFIX
    ENV: str = 'development'
    DEBUG: bool = False

    DATABASE_URL: str = 'mysql+pymysql://backend:6W2%2BqkF%2BIU%24DX0_@the-question.rwlb.rds.aliyuncs.com:3306/the-question?charset=utf8mb4'
    LOG_LEVEL: str = 'INFO'
    CORS_ORIGINS: list[str] = ['*']

    SECRET_KEY: str = 'change-me'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    AUTO_CREATE_TABLES: bool = False

    SKILL_CONTENT_MAX_LEN: int = 20000
    PROVIDERS: str = DEFAULT_PROVIDERS_JSON

    @field_validator('CORS_ORIGINS', mode='before')
    @classmethod
    def parse_cors_origins(cls, value):  # type: ignore[override]
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return []
            if value == '*':
                return ['*']
            return [item.strip() for item in value.split(',') if item.strip()]
        return value


AI_DEBUG_LOG_PATH: Path = Path('reports/ai-debug.jsonl')

settings = Settings()
