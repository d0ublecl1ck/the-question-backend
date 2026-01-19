from app.core.config import (
    DEFAULT_API_V1_PREFIX,
    DEFAULT_PROJECT_NAME,
    DEFAULT_PROVIDERS_JSON,
    Settings,
)
from app.core.providers import _parse_providers


def test_default_providers_json_parses():
    providers = _parse_providers(DEFAULT_PROVIDERS_JSON)
    hosts = {provider.host for provider in providers}
    assert "openai" in hosts
    assert "minimax" in hosts


def test_default_project_name_and_prefix(monkeypatch):
    monkeypatch.delenv("PROJECT_NAME", raising=False)
    monkeypatch.delenv("API_V1_PREFIX", raising=False)
    settings = Settings(_env_file=None)
    assert settings.PROJECT_NAME == DEFAULT_PROJECT_NAME
    assert settings.API_V1_PREFIX == DEFAULT_API_V1_PREFIX
