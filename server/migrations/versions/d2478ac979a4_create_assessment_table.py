"""create assessment table

Revision ID: d2478ac979a4
Revises: 9a17618b2bb9
Create Date: 2022-09-26 14:48:18.575045

"""
from email.policy import default
from operator import index
from alembic import op
import sqlalchemy as sa

from server.core.models import question, label


# revision identifiers, used by Alembic.
revision = 'd2478ac979a4'
down_revision = '9a17618b2bb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "assessments",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("owner_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("hashed_id", sa.String(200), unique=True),
    )
    op.create_table(
        "tests",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("assessment_id", sa.Integer(), sa.ForeignKey("assessments.id"), nullable=False)
    )
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("type", sa.Enum(question.QuestionType), nullable=False),
        sa.Column("description", sa.String(10000), nullable=False)
    )
    op.create_table(
        "answers",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("question_id", sa.Integer(), sa.ForeignKey("questions.id"), nullable=False),
        sa.Column("description", sa.String(10000), nullable=False)
    )
    op.create_table(
        "labels",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("type", sa.Enum(label.LabelType), nullable=False),
        sa.Column("label", sa.String(100), unique=True, nullable=False),
        sa.Column("description", sa.String(10000))
    )
    op.create_table(
        "answer2label",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("answer_id", sa.Integer(), sa.ForeignKey("answers.id"), nullable=False, index=True),
        sa.Column("label_id", sa.Integer(), sa.ForeignKey("labels.id"), nullable=False, index=True),
        sa.Column("score", sa.Integer(), nullable=False, default=0)
    )
    op.create_table(
        "test2question",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("test_id", sa.Integer(), sa.ForeignKey("tests.id"), nullable=False, index=True),
        sa.Column("question_id", sa.Integer(), sa.ForeignKey("questions.id"), nullable=False, index=True)
    )
    
    op.create_foreign_key("test_assessment_fk", source_table="tests", referent_table="assessments",
                          local_cols=["assessment_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")
    op.create_foreign_key("answer_question_fk", source_table="answers", referent_table="questions",
                          local_cols=["question_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")
    op.create_foreign_key("answer2label_answer_fk", source_table="answer2label", referent_table="answers",
                          local_cols=["answer_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")
    op.create_foreign_key("answer2label_label_fk", source_table="answer2label", referent_table="labels",
                          local_cols=["label_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")
    op.create_foreign_key("test2question_test_fk", source_table="test2question", referent_table="tests",
                          local_cols=["test_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")
    op.create_foreign_key("test2question_question_fk", source_table="test2question", referent_table="questions",
                          local_cols=["question_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")


def downgrade() -> None:
    pass
