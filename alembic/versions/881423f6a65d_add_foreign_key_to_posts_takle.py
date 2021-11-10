"""add foreign-key to posts takle

Revision ID: 881423f6a65d
Revises: 2d540b18fc55
Create Date: 2021-11-09 17:07:30.161932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '881423f6a65d'
down_revision = '2d540b18fc55'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
