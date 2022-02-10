""" rename npcs

Revision ID: 7462b5348a50
Revises: 98069582e7e9
Create Date: 2022-02-08 19:21:14.717010

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7462b5348a50'
down_revision = '98069582e7e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('np_cs', 'npcs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('npcs', 'np_cs')
    # ### end Alembic commands ###
