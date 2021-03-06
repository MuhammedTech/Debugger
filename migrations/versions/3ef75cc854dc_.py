"""empty message

Revision ID: 3ef75cc854dc
Revises: a44939c78859
Create Date: 2020-08-07 20:47:40.288801

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '3ef75cc854dc'
down_revision = 'a44939c78859'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('author', sa.Integer(), nullable=False))
    op.alter_column('comment', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'comment', 'comment', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.alter_column('comment', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('comment', 'author')
    # ### end Alembic commands ###
