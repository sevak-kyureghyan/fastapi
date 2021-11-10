"""add content column to posts table

Revision ID: f7dca31fb146
Revises: d7705cea1cea
Create Date: 2021-11-09 16:50:13.622203

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = 'f7dca31fb146'
down_revision = 'd7705cea1cea'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
