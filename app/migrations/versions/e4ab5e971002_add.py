"""add

Revision ID: e4ab5e971002
Revises: ef167a41c084
Create Date: 2024-05-26 14:44:47.858213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e4ab5e971002'
down_revision: Union[str, None] = 'ef167a41c084'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invoices', 'file',
               existing_type=postgresql.BYTEA(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invoices', 'file',
               existing_type=postgresql.BYTEA(),
               nullable=False)
    # ### end Alembic commands ###
