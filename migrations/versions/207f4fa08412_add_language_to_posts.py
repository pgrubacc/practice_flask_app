"""add language to posts

Revision ID: 207f4fa08412
Revises: 93ecc210eec2
Create Date: 2018-07-08 17:20:19.817992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207f4fa08412'
down_revision = '93ecc210eec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
