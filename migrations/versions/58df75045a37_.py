"""empty message

Revision ID: 58df75045a37
Revises: 353cac3c2f3d
Create Date: 2020-08-06 15:58:17.119773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58df75045a37'
down_revision = '353cac3c2f3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'ticket_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###