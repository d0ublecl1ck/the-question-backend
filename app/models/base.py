from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy.dialects.mysql import DATETIME as MySQLDateTime
from sqlmodel import Field, SQLModel


def _utc_now():
    return datetime.now(timezone.utc)


class IDModel(SQLModel):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)


class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=_utc_now,
        sa_type=DateTime(timezone=True).with_variant(MySQLDateTime(fsp=6), "mysql"),
        sa_column_kwargs={"nullable": False},
    )
    updated_at: datetime = Field(
        default_factory=_utc_now,
        sa_type=DateTime(timezone=True).with_variant(MySQLDateTime(fsp=6), "mysql"),
        sa_column_kwargs={"nullable": False, "onupdate": _utc_now},
    )
