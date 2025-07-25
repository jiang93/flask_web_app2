"""initial migrate

Revision ID: 01637510aca9
Revises: 48223f6b5235
Create Date: 2025-07-14 17:32:30.172994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01637510aca9'
down_revision = '48223f6b5235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    # ### end Alembic commands ###
