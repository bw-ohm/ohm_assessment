"""Update some user data

Revision ID: 4f74bf3aa9fc
Revises: 00000000
Create Date: 2020-01-29 14:08:37.465181

"""

# revision identifiers, used by Alembic.
revision = '4f74bf3aa9fc'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute("UPDATE user SET point_balance = 5000 WHERE user_id = 1")
    op.execute("INSERT INTO rel_user (user_id, rel_lookup, attribute) VALUES (2, 'LOCATION', 'USA')")
    op.execute("UPDATE user SET tier = 'Silver' WHERE user_id = 3")

def downgrade():
    op.execute("UPDATE user SET point_balance = 0 WHERE user_id = 1")
    op.execute("DELETE FROM rel_user WHERE user_id = 2 AND rel_lookup = 'LOCATION' AND attribute = 'USA'")
    op.execute("UPDATE user SET tier = 'Carbon' WHERE user_id = 3")
