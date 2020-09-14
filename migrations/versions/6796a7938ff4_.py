"""empty message

Revision ID: 6796a7938ff4
Revises: 451191a8ba6c
Create Date: 2020-08-14 19:00:03.342562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6796a7938ff4'
down_revision = '451191a8ba6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'parent_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('comment', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('comment', 'timestamp',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.create_index(op.f('ix_comment_path'), 'comment', ['path'], unique=False)
    op.create_foreign_key(None, 'comment', 'comment', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_index(op.f('ix_comment_path'), table_name='comment')
    op.alter_column('comment', 'timestamp',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.alter_column('comment', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comment', 'parent_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
