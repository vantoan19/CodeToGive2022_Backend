"""create user table

Revision ID: 9a17618b2bb9
Revises: 
Create Date: 2022-09-26 13:40:01.763647

"""
import sqlalchemy as sa
from alembic import op
from server.core.models import user

# revision identifiers, used by Alembic.
revision = '9a17618b2bb9'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, index=True, nullable=False),
        sa.Column("email", sa.String(100), unique=True, index=True, nullable=False),
        sa.Column("account_type", sa.Enum(user.AccountType), default=user.AccountType.USER),
        sa.Column("account_status", sa.Enum(user.AccountStatus), default=user.AccountStatus.NOT_REGISTERED),
        sa.Column("first_name", sa.String(50)),
        sa.Column("last_name", sa.String(50)),
    )
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), primary_key=True, index=True, nullable=False),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id")),
        sa.Column("street_line_1", sa.String(100)),
        sa.Column("street_line_2", sa.String(100)),
        sa.Column("district", sa.String(30)),
        sa.Column("city", sa.String(30)),
        sa.Column("region", sa.String(30)),
        sa.Column("country", sa.String(30))
    )
    
    op.create_foreign_key("address_user_fk", source_table="addresses", referent_table="users", 
                          local_cols=["user_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_user_fk", table_name="users")
    op.drop_table("addresses")
    op.drop_table("users")
