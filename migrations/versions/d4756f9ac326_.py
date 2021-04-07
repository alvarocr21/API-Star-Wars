"""empty message

Revision ID: d4756f9ac326
Revises: 9077e9f94ec2
Create Date: 2021-04-06 04:41:46.138033

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd4756f9ac326'
down_revision = '9077e9f94ec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favoritos', 'nombre')
    op.drop_column('favoritos', 'id_tipo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favoritos', sa.Column('id_tipo', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('favoritos', sa.Column('nombre', mysql.VARCHAR(length=120), nullable=False))
    # ### end Alembic commands ###
