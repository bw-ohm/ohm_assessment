"""add index to rel_user_multi

Revision ID: 8a4b5dee52f
Revises: 4f74bf3aa9fc
Create Date: 2020-01-30 15:01:17.078294

"""

# revision identifiers, used by Alembic.
revision = '8a4b5dee52f'
down_revision = '4f74bf3aa9fc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index('ix_rel_user_multi_user_id', 'rel_user_multi', ['user_id'])

def downgrade():
    op.drop_index('ix_rel_user_multi_user_id', 'rel_user_multi')
