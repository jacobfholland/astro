"""empty message

Revision ID: f595cfd3870d
Revises: 284246143fa9
Create Date: 2023-01-30 20:50:03.633441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f595cfd3870d'
down_revision = '284246143fa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('adult', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('backdrop_path', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('budget', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('homepage', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('imdb_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('original_language', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('original_title', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('popularity', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('poster_path', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('release_date', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('revenue', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('runtime', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('status', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('tagline', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movie', schema=None) as batch_op:
        batch_op.drop_column('tagline')
        batch_op.drop_column('status')
        batch_op.drop_column('runtime')
        batch_op.drop_column('revenue')
        batch_op.drop_column('release_date')
        batch_op.drop_column('poster_path')
        batch_op.drop_column('popularity')
        batch_op.drop_column('original_title')
        batch_op.drop_column('original_language')
        batch_op.drop_column('imdb_id')
        batch_op.drop_column('homepage')
        batch_op.drop_column('budget')
        batch_op.drop_column('backdrop_path')
        batch_op.drop_column('adult')

    # ### end Alembic commands ###
