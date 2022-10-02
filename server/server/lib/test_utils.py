from server.core import schemas


def get_completed(questions: schemas.QuestionWithAnsweredId) -> bool:
    for question in questions:
        if not question.answered_id:
            return False
    return True

def get_progress(questions: schemas.QuestionWithAnsweredId) -> int:
    number_of_answered_question = 0
    for question in questions:
        number_of_answered_question += 1 if question.answered_id else 0
    return number_of_answered_question * 100 // len(questions)
