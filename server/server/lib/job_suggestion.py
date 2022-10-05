from collections import defaultdict
from typing import List
from unittest import result
from server.core.models import TestType, Job
from server.core import schemas
from server.core.schemas import Test, AnswerWithLabels, LabelWithTotalScore
from server.crud import (
    assessment_crud,
    job_crud,
    question_crud,
    test_crud,
    answer_crud,
    label_crud,
)
from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from functools import cmp_to_key
import logging

types_of_test = [
    TestType.MOTIVATION_TEST,
    TestType.ENGLISH_TEST,
    TestType.SOCIAL_SITUATION_TEST,
    TestType.VISIO_PERCEPTUAL_TEST,
]


def find_job_label(label: str, job: Job) -> str | None:
    for job_label in job.labels:
        if job_label.label == label:
            return job_label
    return None


def count_achieved_labels(label_scores: defaultdict, job: Job):
    label_cnt = 0
    for key in label_scores:
        job_label = find_job_label(key, job)
        logging.info(f"LOW: {(job_label.lower_importance_bound-1)*20}")
        logging.info(f"UP: {(job_label.upper_importance_bound)*20}")
        logging.info(f"Score: {label_scores[key]}")
        if (
            (job_label.lower_importance_bound - 1) * 20
            <= label_scores[key]
            < job_label.upper_importance_bound * 20
        ):
            label_cnt += 1
    logging.info(f"CNT: {label_cnt}")
    logging.info(job.title)
    return label_cnt


def compare(a: Job, b: Job, label_scores: defaultdict):
    if count_achieved_labels(label_scores=label_scores, job=a) > count_achieved_labels(
        label_scores=label_scores, job=b
    ):
        return -1
    elif count_achieved_labels(
        label_scores=label_scores, job=a
    ) < count_achieved_labels(label_scores=label_scores, job=b):
        return 1
    else:
        return 0


def get_suggestion_jobs_for_assessment(db: Session, uuid: str):
    label_scores = defaultdict(int)
    label_max_scores = defaultdict(int)
    for test_type in types_of_test:
        test_db = test_crud.get_test_of_an_assessment(
            db=db, test_type=test_type, uuid=uuid
        )
        if not test_db:
            continue
        test = Test.from_orm(test_db)
        for question in test.questions:
            if not question.answered_id:
                continue
            answered_db = answer_crud.get(db=db, id=question.answered_id)
            answered = AnswerWithLabels.from_orm(answered_db)
            for label in answered.labels:
                label_scores[label.label] += label.score
                label_max_scores[label.label] += label.max_score
    label_actual_scores = defaultdict(int)
    for key in label_scores:
        label_actual_scores[key] = (
            0
            if label_max_scores[key] == 0
            else label_scores[key] * 100 // label_max_scores[key]
        )
    all_jobs = parse_obj_as(List[schemas.Job], job_crud.get_multi(db=db))
    binded_compare = lambda a, b: compare(a=a, b=b, label_scores=label_actual_scores)
    return sorted(all_jobs, key=cmp_to_key(binded_compare))[:8]


def get_assessment_report(db: Session, uuid: str) -> List[LabelWithTotalScore]:
    label_scores = defaultdict(int)
    label_max_scores = defaultdict(int)
    for label in label_crud.get_multi(db=db):
        label_scores[label.label] = 0
        label_max_scores[label.label] = 0
    for test_type in types_of_test:
        test_db = test_crud.get_test_of_an_assessment(
            db=db, test_type=test_type, uuid=uuid
        )
        if not test_db:
            continue
        test = Test.from_orm(test_db)
        for question in test.questions:
            if not question.answered_id:
                continue
            answered_db = answer_crud.get(db=db, id=question.answered_id)
            answered = AnswerWithLabels.from_orm(answered_db)
            for label in answered.labels:
                label_scores[label.label] += label.score
                label_max_scores[label.label] += label.max_score
    result = []
    for key in label_scores:
        result.append(
            LabelWithTotalScore(
                label=key,
                total_score=label_scores[key],
                total_max_score=label_max_scores[key],
            )
        )
    return result
