"""create job table

Revision ID: 7d502beb72cd
Revises: d2478ac979a4
Create Date: 2022-10-03 01:32:38.487905

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '7d502beb72cd'
down_revision = 'd2478ac979a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), primary_key=True, index=True, nullable=False),
        sa.Column("title", sa.String(2000), nullable=False),
        sa.Column("description", sa.String(2000), nullable=False),
        sa.Column("company_name", sa.String(200), nullable=False),
        sa.Column("company_about", sa.String(2000)),
        sa.Column("image", sa.String(500)),
    )
    op.create_table(
        "job2label",
        sa.Column("job_id", sa.Integer(), sa.ForeignKey("jobs.id"), index=True, nullable=False),
        sa.Column("label_id", sa.Integer(), sa.ForeignKey("labels.id"), index=True, nullable=False),
        sa.Column("lower_importance_bound", sa.Integer(), default=1),
        sa.Column("upper_importance_bound", sa.Integer(), default=5)
    )
    op.add_column("addresses", sa.Column("job_id", sa.Integer(), sa.ForeignKey("jobs.id"), nullable=True))
    op.create_foreign_key("address_job_fk", source_table="addresses", referent_table="jobs",
                          local_cols=["job_id"], remote_cols=["id"], ondelete="CASCADE", onupdate="CASCADE")
    op.create_foreign_key("job2label_job_fk", source_table="job2label", referent_table="jobs",
                          local_cols=["job_id"], remote_cols=["id"], ondelete="CASCADE", onupdate="CASCADE")
    op.create_foreign_key("job2label_label_fk", source_table="job2label", referent_table="labels",
                          local_cols=["label_id"], remote_cols=["id"], ondelete="CASCADE", onupdate="CASCADE")

def downgrade() -> None:
    op.drop_constraint()
