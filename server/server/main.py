from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mock_objects.mock_objects as mock_objects

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mock_jobs = mock_objects["mock_jobs"]
mock_assessments = mock_objects["mock_assessments"]


@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World!"}


@app.get("/api/v1/user/suggested-jobs" )
async def get_jobs():
    return mock_jobs



@app.get("/api/v1/user/assessments" )
async def get_jobs():
    return mock_assessments