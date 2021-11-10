"""add last few columns to posts table

Revision ID: 75dfd06be474
Revises: 881423f6a65d
Create Date: 2021-11-09 17:16:34.650117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75dfd06be474'
down_revision = '881423f6a65d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
