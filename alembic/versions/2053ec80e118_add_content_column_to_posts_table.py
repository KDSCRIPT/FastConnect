"""add content column to posts table

Revision ID: 2053ec80e118
Revises: a22ff3cd37ea
Create Date: 2025-07-21 08:41:51.699327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2053ec80e118'
down_revision: Union[str, Sequence[str], None] = 'a22ff3cd37ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts","content")
    pass
