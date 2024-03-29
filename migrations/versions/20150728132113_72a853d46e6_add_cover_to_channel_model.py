"""Add cover to Channel model.

Revision ID: 72a853d46e6
Revises: 2c59b20c5ab1
Create Date: 2015-07-28 13:21:13.772917

"""

# revision identifiers, used by Alembic.
revision = '72a853d46e6'
down_revision = '2c59b20c5ab1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channel', sa.Column('cover', sa.String(length=200), nullable=True))
    op.drop_constraint(u'channel_comment_ibfk_1', 'channel_comment', type_='foreignkey')
    op.create_foreign_key(None, 'channel_comment', 'channel', ['channel_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'channel_comment', type_='foreignkey')
    op.create_foreign_key(u'channel_comment_ibfk_1', 'channel_comment', 'piece', ['channel_id'], ['id'])
    op.drop_column('channel', 'cover')
    ### end Alembic commands ###
