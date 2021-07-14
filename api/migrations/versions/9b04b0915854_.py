"""empty message

Revision ID: 9b04b0915854
Revises: d84abcbcf722
Create Date: 2021-07-14 15:09:59.103822

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utc


# revision identifiers, used by Alembic.
revision = '9b04b0915854'
down_revision = 'd84abcbcf722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role_permission')
    op.drop_table('permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role_permission',
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.permission_id'], name='role_permission_permission_id_fkey'),
    sa.ForeignKeyConstraint(['role_id'], ['role.role_id'], name='role_permission_role_id_fkey'),
    sa.PrimaryKeyConstraint('role_id', 'permission_id', name='role_permission_pkey')
    )
    op.create_table('permission',
    sa.Column('permission_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('permission_code', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('permission_desc', sa.VARCHAR(length=1000), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('permission_id', name='permission_pkey')
    )
    # ### end Alembic commands ###
