"""v3

Revision ID: a1f4a831cf8e
Revises: 9587c36e3083
Create Date: 2023-11-22 19:31:06.955168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f4a831cf8e'
down_revision = '9587c36e3083'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('surat_masuk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomor_surat', sa.String(length=20), nullable=True),
    sa.Column('tgl_surat', sa.DateTime(), nullable=True),
    sa.Column('jenis', sa.String(length=20), nullable=True),
    sa.Column('keterangan', sa.String(length=55), nullable=True),
    sa.Column('url_docx', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('surat_masuk')
    # ### end Alembic commands ###
