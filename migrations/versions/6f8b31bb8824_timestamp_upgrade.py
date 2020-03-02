"""timestamp upgrade

Revision ID: 6f8b31bb8824
Revises: 7910158e2556
Create Date: 2020-03-01 03:56:42.221843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f8b31bb8824'
down_revision = '7910158e2556'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'timestamp', type_='foreignkey')
    op.create_foreign_key(None, 'timestamp', 'laundry', ['item_id'], ['id'])
    op.drop_index(op.f('ix_timestamp_status'), table_name='timestamp')
    op.drop_column('timestamp', 'status')
    op.drop_index(op.f('ix_search_status'), table_name='search')
    op.drop_index(op.f('ix_search_item_type'), table_name='search')
    op.drop_index(op.f('ix_search_item_size'), table_name='search')
    op.drop_index(op.f('ix_search_item_note'), table_name='search')
    # ### end Alembic commands ###
