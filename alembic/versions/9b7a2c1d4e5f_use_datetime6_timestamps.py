"""use datetime6 timestamps

Revision ID: 9b7a2c1d4e5f
Revises: 7f3d2b1c9e8f, 8140ad6478a8
Create Date: 2026-01-22 00:15:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision: str = '9b7a2c1d4e5f'
down_revision: Union[str, Sequence[str], None] = ('7f3d2b1c9e8f', '8140ad6478a8')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


_TABLES: tuple[str, ...] = (
    'chat_messages',
    'chat_sessions',
    'memories',
    'notifications',
    'refresh_tokens',
    'reports',
    'skill_comments',
    'skill_favorites',
    'skill_ratings',
    'skill_suggestions',
    'skill_versions',
    'skills',
    'users',
    'skill_draft_suggestions',
)


def _target_type(dialect_name: str) -> sa.types.TypeEngine:
    if dialect_name == 'mysql':
        return mysql.DATETIME(fsp=6)
    return sa.DateTime()


def _downgrade_type(dialect_name: str) -> sa.types.TypeEngine:
    if dialect_name == 'mysql':
        return mysql.DATETIME()
    return sa.DateTime()


def _alter_timestamp_columns(table: str, target_type: sa.types.TypeEngine) -> None:
    op.alter_column(
        table,
        'created_at',
        existing_type=sa.DateTime(),
        type_=target_type,
        nullable=False,
    )
    op.alter_column(
        table,
        'updated_at',
        existing_type=sa.DateTime(),
        type_=target_type,
        nullable=False,
    )


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    dialect_name = bind.dialect.name if bind is not None else ''
    target_type = _target_type(dialect_name)
    for table in _TABLES:
        _alter_timestamp_columns(table, target_type)


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    dialect_name = bind.dialect.name if bind is not None else ''
    target_type = _downgrade_type(dialect_name)
    for table in _TABLES:
        _alter_timestamp_columns(table, target_type)
