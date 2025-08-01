"""create posts table

Revision ID: a22ff3cd37ea
Revises: 
Create Date: 2025-07-18 19:42:47.038508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a22ff3cd37ea'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column("title",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    """Downgrade schema."""
    pass
