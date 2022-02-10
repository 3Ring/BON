"""create new bridge tables

Revision ID: 59ae6e0b35cd
Revises: bed97e30bb1d
Create Date: 2022-02-08 20:11:40.043307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59ae6e0b35cd'
down_revision = 'bed97e30bb1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bridgeuserimages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('removed', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('img_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['img_id'], ['images.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bridgegamecharacters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('removed', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('dm', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bridgegameitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('removed', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bridgegamenpcs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('removed', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('npc_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['npc_id'], ['npcs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bridgegameplaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('removed', sa.Boolean(), server_default=sa.text('FALSE'), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('place_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['place_id'], ['places.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bridgegameplaces')
    op.drop_table('bridgegamenpcs')
    op.drop_table('bridgegameitems')
    op.drop_table('bridgegamecharacters')
    op.drop_table('bridgeuserimages')
    # ### end Alembic commands ###
