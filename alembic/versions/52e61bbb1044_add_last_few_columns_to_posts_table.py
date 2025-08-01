"""add last few columns to posts table

Revision ID: 52e61bbb1044
Revises: 364ad758d74a
Create Date: 2025-07-21 09:15:20.710987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52e61bbb1044'
down_revision: Union[str, Sequence[str], None] = '364ad758d74a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False,server_default="TRUE"))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("NOW()")))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    """Downgrade schema."""
    pass
