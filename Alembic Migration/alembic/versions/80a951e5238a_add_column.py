"""add column

Revision ID: 80a951e5238a
Revises: 23785914bb40
Create Date: 2022-12-12 12:49:18.322475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80a951e5238a'
down_revision = '23785914bb40'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.add_column('account', sa.Column('created_at', sa.DateTime))
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))
    pass


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
    pass
