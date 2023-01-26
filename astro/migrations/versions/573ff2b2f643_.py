"""empty message

Revision ID: 573ff2b2f643
Revises: 
Create Date: 2023-01-22 04:51:17.944735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573ff2b2f643'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
