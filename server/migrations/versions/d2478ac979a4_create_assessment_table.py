"""create assessment table

Revision ID: d2478ac979a4
Revises: 9a17618b2bb9
Create Date: 2022-09-26 14:48:18.575045

"""
from email.policy import default
from operator import index

import sqlalchemy as sa
from alembic import op
from server.core.models import label, question, test

# revision identifiers, used by Alembic.
revision = 'd2478ac979a4'
down_revision = '9a17618b2bb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "assessments",
        sa.Column("owner_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("uuid", sa.String(200), primary_key=True, index=True, unique=True),
    )
    op.create_table(
        "tests",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("title", sa.String(2000)),
        sa.Column("assessment_uuid", sa.String(200), sa.ForeignKey("assessments.uuid"), nullable=False),
        sa.Column("type", sa.dialects.mysql.ENUM(test.TestType), nullable=False),
        sa.Column("description", sa.String(10000))
    )
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("type", sa.dialects.mysql.ENUM(question.QuestionType), nullable=False),
        sa.Column("description", sa.String(10000), nullable=False),
        sa.Column("img_url", sa.String(500)),
        sa.Column("img_alt", sa.String(2000))
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
        sa.Column("type", sa.dialects.mysql.ENUM(label.LabelType), nullable=False),
        sa.Column("label", sa.String(100), unique=True, nullable=False),
        sa.Column("description", sa.String(10000))
    )
    op.create_table(
        "answer2label",
        sa.Column("answer_id", sa.Integer(), sa.ForeignKey("answers.id"), primary_key=True, nullable=False, index=True),
        sa.Column("label_id", sa.Integer(), sa.ForeignKey("labels.id"), primary_key=True, nullable=False, index=True),
        sa.Column("score", sa.Integer(), nullable=False, default=0)
    )
    op.create_table(
        "test2question",
        sa.Column("test_id", sa.Integer(), sa.ForeignKey("tests.id"), primary_key=True, nullable=False, index=True),
        sa.Column("question_id", sa.Integer(), sa.ForeignKey("questions.id"), primary_key=True, nullable=False, index=True),
        sa.Column("answered_id", sa.Integer(), sa.ForeignKey("answers.id"), nullable=True, default=None)
    )
    
    op.create_foreign_key("test_assessment_fk", source_table="tests", referent_table="assessments",
                          local_cols=["assessment_uuid"], remote_cols=["uuid"], onupdate="CASCADE", ondelete="CASCADE")
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
    op.create_foreign_key("test2question_answer_fk", source_table="test2question", referent_table="answers",
                          local_cols=["answered_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="CASCADE")
    op.create_foreign_key("assessment_user_fk", source_table="assessments", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], onupdate="CASCADE", ondelete="RESTRICT")


def downgrade() -> None:
    op.drop_constraint("test2question_answer_fk", table_name="answers")
    op.drop_constraint("test2question_question_fk", table_name="questions")
    op.drop_constraint("test2question_test_fk", table_name="tests")
    op.drop_constraint("answer2label_label_fk", table_name="labels")
    op.drop_constraint("answer2label_answer_fk", table_name="answers")
    op.drop_constraint("answer_question_fk", table_name="questions")
    op.drop_constraint("test_assessment_fk", table_name="assessments")
    op.drop_table("test2question")
    op.drop_table("answer2label")
    op.drop_table("labels")
    op.drop_table("answers")
    op.drop_table("questions")
    op.drop_table("tests")
    op.drop_table("assessments")
