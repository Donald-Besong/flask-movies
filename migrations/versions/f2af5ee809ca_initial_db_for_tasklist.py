"""initial db for tasklist

Revision ID: f2af5ee809ca
Revises: 
Create Date: 2023-03-25 12:33:40.570419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2af5ee809ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_list', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               type_=sa.String(length=64),
               nullable=True)
        batch_op.create_index(batch_op.f('ix_task_list_name'), ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_list', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task_list_name'))
        batch_op.alter_column('name',
               existing_type=sa.String(length=64),
               type_=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    # ### end Alembic commands ###