"""v2

Revision ID: 9587c36e3083
Revises: 6db8b1ec784e
Create Date: 2023-11-22 19:27:43.022510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9587c36e3083'
down_revision = '6db8b1ec784e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('surat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomor_surat', sa.String(length=20), nullable=True),
    sa.Column('tgl_surat', sa.DateTime(), nullable=True),
    sa.Column('jenis', sa.String(length=20), nullable=True),
    sa.Column('keterangan', sa.String(length=55), nullable=True),
    sa.Column('url_docx', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=168),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=168),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    op.drop_table('surat')
    # ### end Alembic commands ###
