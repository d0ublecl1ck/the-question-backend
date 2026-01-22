from sqlalchemy import create_engine, inspect

from app.core import config as config_module
from app.db import init_db as init_module


def test_init_db_creates_tables_for_sqlite_in_production(monkeypatch):
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    monkeypatch.setattr(init_module, "engine", engine)
    monkeypatch.setattr(config_module.settings, "ENV", "production")
    monkeypatch.setattr(config_module.settings, "DATABASE_URL", "sqlite:///:memory:")

    init_module.init_db(drop_all=True)

    inspector = inspect(engine)
    assert "users" in inspector.get_table_names()


def test_init_db_creates_tables_when_auto_create_enabled(monkeypatch):
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    monkeypatch.setattr(init_module, "engine", engine)
    monkeypatch.setattr(config_module.settings, "ENV", "production")
    monkeypatch.setattr(
        config_module.settings,
        "DATABASE_URL",
        "mysql+pymysql://backend:6W2%2BqkF%2BIU%24DX0_@the-question.rwlb.rds.aliyuncs.com:3306/the-question?charset=utf8mb4",
    )
    monkeypatch.setattr(config_module.settings, "AUTO_CREATE_TABLES", True)

    init_module.init_db(drop_all=True)

    inspector = inspect(engine)
    assert "users" in inspector.get_table_names()
