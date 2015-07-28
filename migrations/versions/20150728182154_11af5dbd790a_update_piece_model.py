"""Update piece model.

Revision ID: 11af5dbd790a
Revises: 1af2d63b2556
Create Date: 2015-07-28 18:21:54.612753

"""

# revision identifiers, used by Alembic.
revision = '11af5dbd790a'
down_revision = '1af2d63b2556'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('piece', sa.Column('desc', sa.Text(), nullable=True))
    op.add_column('piece', sa.Column('image', sa.String(length=200), nullable=True))
    op.add_column('piece', sa.Column('kind', sa.Enum('TEXT', 'IMAGE'), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('piece', 'kind')
    op.drop_column('piece', 'image')
    op.drop_column('piece', 'desc')
    ### end Alembic commands ###