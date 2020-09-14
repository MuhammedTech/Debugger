"""empty message

Revision ID: a44939c78859
Revises: 1b5c0ce7a795
Create Date: 2020-08-07 20:38:26.226507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a44939c78859'
down_revision = '1b5c0ce7a795'
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
