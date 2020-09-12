"""empty message

Revision ID: 3280dd894da0
Revises: ded54e0e55a8
Create Date: 2020-08-17 23:32:02.557292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3280dd894da0'
down_revision = 'ded54e0e55a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'timestamp',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.drop_column('comment', 'parent_id')
    op.drop_column('comment', 'path')
    op.alter_column('files', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('files', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('comment', sa.Column('path', sa.TEXT(), nullable=True))
    op.add_column('comment', sa.Column('parent_id', sa.INTEGER(), nullable=True))
    op.alter_column('comment', 'timestamp',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###