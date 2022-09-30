from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from mock_data import mock_jobs,mock_work_motivation_test 

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World!"}


@app.get("/api/v1/user/suggested-jobs" )
async def get_jobs():
    return mock_jobs

@app.get("/api/v1/user/work-motivation-test/assessment" )
async def get_jobs():
    return mock_work_motivation_test

