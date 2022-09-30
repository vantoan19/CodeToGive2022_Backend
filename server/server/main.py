from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mock_jobs = [{
    "id": 1,
    "label": "Librarian",
    "match_value": 72,
    "details": {
      "company_name": "Canary inc.",
      "about": "This company is legit, no cap, 4real",
      "description": "U will need to do this, and that, this skill, that skill"
    },
    "image": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGlicmFyeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
  },
  {
    "id": 2,
    "label": "Recptionist",
    "match_value": 60,
    "details": {
        "company_name": "Dunder Mifflin Inc.",
        "about": "Paper company",
        "description": "Answer the phone, make some copies,etc.",
    },
    "image": "https://images.unsplash.com/photo-1556741533-6e6a62bd8b49?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cmVjZXB0aW9uaXN0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
  },
  {
    "id": 3,
    "label": "Bartender",
    "match_value": 90,
    "details": {
        "company_name": "Black Box",
        "about": "Club",
        "description": "Make and serves drinks"
    },
    "image": "https://images.unsplash.com/photo-1595751866979-de6e9d606220?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YmFydGVuZGVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
  }
  ]


mock_work_motivation_test = {
  "test_id": 1,
  "title": "Work motivation test",
  "questions": [
    {
      "type": "MOTIVATION_QUESTION",
      "description": "Question1",
      "question_id": 12,
      "answered_value": 125,
      "answers": [
        {
          "description": "1",
          "answer_id": 123,
          "question_id": 12,
          "test_id":1
        },
        {
          "description": "2",
          "answer_id": 124,
          "question_id": 12,
          "test_id":1
        },
        {
          "description": "3",
          "answer_id": 125,
          "question_id": 12,
          "test_id":1
        },
        {
          "description": "4",
          "answer_id": 126,
          "question_id": 12,
          "test_id":1
        },
        {
          "description": "5",
          "answer_id": 127,
          "question_id": 12,
          "test_id":1
        },
      ],
      "image": {
        "src": "https://images.unsplash.com/photo-1556741533-6e6a62bd8b49?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cmVjZXB0aW9uaXN0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "alt": "Alt text",
      },
    },
    {
      "type": "MOTIVATION_QUESTION",
      "description": "Question2",
      "question_id": 13,

      "answers": [
        {
          "description": "1",
          "answer_id": 128,
          "question_id": 13,
          "test_id":1
        },
        {
          "description": "2",
          "answer_id": 129,
          "question_id": 13,
          "test_id":1
        },
        {
          "description": "3",
          "answer_id": 130,
          "question_id": 13,
          "test_id":1
        },
        {
          "description": "4",
          "answer_id": 131,
          "question_id": 13,
          "test_id":1
        },
        {
          "description": "5",
          "answer_id": 132,
          "question_id": 13,
          "test_id":1
        },
      ],
      "image": {
        "src": "https://images.unsplash.com/photo-1664555723834-ec251e81a3ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1199&q=80",
        "alt": "Alt text",
      },
    },
    {
      "type": "MOTIVATION_QUESTION",
      "description": "Question3",
      "question_id": 14,

      "answers": [
        {
          "description": "1",
          "answer_id": 133,
          "question_id": 14,
          "test_id":1
        },
        {
          "description": "2",
          "answer_id": 134,
          "question_id": 14,
          "test_id":1
        },
        {
          "description": "3",
          "answer_id": 135,
          "question_id": 14,
          "test_id":1
        },
        {
          "description": "4",
          "answer_id": 136,
          "question_id": 14,
          "test_id":1
        },
        {
          "description": "5",
          "answer_id": 137,
          "question_id": 14,
          "test_id":1
        },
      ],
      "image": {
        "src": "https://images.unsplash.com/photo-1657299143471-231353519c63?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        "alt": "Alt text",
      },
    },
  ],
}

mock_assessments = [
  {
    "title": "Work motivation test",
    "url": "/assessments/work-motivation",
    "description":
      "Tell more about your interests so you can find the most suitable job.",
    "completed": False,
    "icon": {
      "name": "WorkOutlineIcon",
      "color":
        "radial-gradient(102.34% 102.34% at 50% 50%, #3BC49A 0%, #158787 100%)",
    },
    "progress": 20,
  },
  {
    "title": "English language test",
    "url": "/assessments/english-language-test",
    "description":
      "You will be asked some questions about English situations to measure your knowledge.",
    "completed": False,
    "icon": {
      "name": "TranslateIcon",
      "color":
        "radial-gradient(102.34% 102.34% at 50% 50%, #DA87AF 0%, #802C59 100%)",
    },
    "progress": 0,
  },
  {
    "title": "Visio-perceptual skills",
    "url": "/assessments/visio-perceptual-skills",
    "description": "We will measure your sight and hearing.",
    "completed": False,
    "icon": {
      "name": "VisibilityOutlinedIcon",
      "color":
        "radial-gradient(102.34% 102.34% at 50% 50%, #1D66D3 0%, #06459F 100%)",
    },
    "progress": 80,
  },
  {
    "title": "Some other test",
    "url": "/assessments/other-tests",
    "description": "This is some other random test to observe your capabilities.",
    "completed": True,
    "icon": {
      "name": "QuizOutlinedIcon",
      "color":
        "radial-gradient(102.34% 102.34% at 50% 50%, #8B7560 0%, #58390A 100%)",
    },
    "progress": 100,
  },
]

mock_uuid = {
  "uuid": "1234"
}

@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World!"}


@app.get("/api/v1/{uuid}/suggested-jobs" )
async def get_jobs(uuid : str):
    return mock_jobs

@app.get("/api/v1/{uuid}/work-motivation-test/assessment" )
async def get_work_motivation_test(uuid : str):
    return mock_work_motivation_test

@app.get("/api/v1/{uuid}/assessments")
async def get_assessments(uuid : str):
  return mock_assessments

@app.get("/api/v1/assessments/generate")
async def get_uuid():
  return mock_uuid
