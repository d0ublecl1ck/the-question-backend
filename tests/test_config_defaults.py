from app.core.config import Settings


def test_default_database_url_includes_charset(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    settings = Settings(_env_file=None)
    assert (
        settings.DATABASE_URL
        == "mysql+pymysql://backend:6W2%2BqkF%2BIU%24DX0_@the-question.rwlb.rds.aliyuncs.com:3306/the-question?charset=utf8mb4"
    )
