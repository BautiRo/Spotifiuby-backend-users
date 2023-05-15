"""Change date_created

Revision ID: bfc5d07103a7
Revises: e1a405c1fcdf
Create Date: 2022-05-18 10:52:34.624374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfc5d07103a7'
down_revision = 'e1a405c1fcdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'date_created')
    # ### end Alembic commands ###
