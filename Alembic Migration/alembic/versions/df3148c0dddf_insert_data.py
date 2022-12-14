"""insert data

Revision ID: df3148c0dddf
Revises: 80a951e5238a
Create Date: 2022-12-12 12:55:34.466461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3148c0dddf'
down_revision = '80a951e5238a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.execute("INSERT INTO account(id, name, description, created_at) VALUES ('1', 'akash', 'good work', '2022-10-13 11:58:05.692487');")
    op.execute("INSERT INTO account(id, name, description, created_at) VALUES ('2', 'bikash', 'very good work', '2022-10-13 11:58:05.692487');")
    # op.execute("DELETE FROM account WHERE id=1")
    pass


def downgrade() -> None:
    op.execute("DELETE FROM account WHERE id=2")
    print("okk")
    pass
