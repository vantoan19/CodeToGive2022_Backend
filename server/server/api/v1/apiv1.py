from fastapi import APIRouter
from server.api.v1.routers import (answer, assessment, label, question, test,
                                   user)

apiv1_router = APIRouter()
apiv1_router.include_router(answer.router, prefix="/answers", tags=["answers"])
apiv1_router.include_router(assessment.router, prefix="/assessments", tags=["assessments"])
apiv1_router.include_router(label.router, prefix="/labels", tags=["labels"])
apiv1_router.include_router(question.router, prefix="/questions", tags=["questions"])
apiv1_router.include_router(test.router, prefix="/tests", tags=["tests"])
apiv1_router.include_router(user.router, prefix="/users", tags=["users"])
