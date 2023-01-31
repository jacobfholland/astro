"""empty message

Revision ID: 284246143fa9
Revises: a5d569687793
Create Date: 2023-01-30 20:47:01.069693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284246143fa9'
down_revision = 'a5d569687793'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('duration')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('duration', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
