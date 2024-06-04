"""add

Revision ID: 8733ed26f9dd
Revises: e4ab5e971002
Create Date: 2024-05-27 02:08:00.208852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8733ed26f9dd'
down_revision: Union[str, None] = 'e4ab5e971002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invoices', sa.Column('electricity_kWh', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('electricity_RS', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('sceee_energy_without_ICMS_kWh', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('sceee_energy_without_ICMS_RS', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('compensated_energy_GD_I_kWh', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('compensated_energy_GD_I_RS', sa.String(), nullable=True))
    op.drop_column('invoices', 'compensated_energy_GD_I')
    op.drop_column('invoices', 'sceee_energy_without_ICMS')
    op.drop_column('invoices', 'electricity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invoices', sa.Column('electricity', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('invoices', sa.Column('sceee_energy_without_ICMS', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('invoices', sa.Column('compensated_energy_GD_I', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('invoices', 'compensated_energy_GD_I_RS')
    op.drop_column('invoices', 'compensated_energy_GD_I_kWh')
    op.drop_column('invoices', 'sceee_energy_without_ICMS_RS')
    op.drop_column('invoices', 'sceee_energy_without_ICMS_kWh')
    op.drop_column('invoices', 'electricity_RS')
    op.drop_column('invoices', 'electricity_kWh')
    # ### end Alembic commands ###