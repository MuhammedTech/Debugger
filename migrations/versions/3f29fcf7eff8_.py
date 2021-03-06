"""empty message

Revision ID: 3f29fcf7eff8
Revises: 13af903d8a1c
Create Date: 2020-08-18 07:54:49.215059

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '3f29fcf7eff8'
down_revision = '13af903d8a1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'path')
    op.drop_column('comment', 'parent_id')
    op.alter_column('files', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('files', 'timestamp',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('files', 'timestamp',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('files', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('comment', sa.Column('parent_id', sa.INTEGER(), nullable=True))
    op.add_column('comment', sa.Column('path', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
