from app.core.config import Settings
from app.core.env import get_env_value


def test_get_env_value_prefers_env_file(monkeypatch, tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("OPENAI_API_KEY=file-key\n", encoding="utf-8")
    monkeypatch.setattr(Settings, "model_config", {"env_file": str(env_path)}, raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "env-key")
    assert get_env_value("OPENAI_API_KEY") == "file-key"


def test_get_env_value_ignores_env_when_env_file_missing_key(monkeypatch, tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("OTHER_KEY=1\n", encoding="utf-8")
    monkeypatch.setattr(Settings, "model_config", {"env_file": str(env_path)}, raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "env-key")
    assert get_env_value("OPENAI_API_KEY") is None


def test_get_env_value_falls_back_to_env_when_env_file_absent(monkeypatch, tmp_path):
    env_path = tmp_path / ".env"
    monkeypatch.setattr(Settings, "model_config", {"env_file": str(env_path)}, raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "env-key")
    assert get_env_value("OPENAI_API_KEY") == "env-key"
