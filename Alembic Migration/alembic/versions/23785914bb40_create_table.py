"""create table

Revision ID: 23785914bb40
Revises: 
Create Date: 2022-12-12 12:46:54.766094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23785914bb40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )
    pass


def downgrade() -> None:
    pass
