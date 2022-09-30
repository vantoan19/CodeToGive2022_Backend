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
  id: 1,
  title: "Work motivation test",
  questions: [
    {
      id: 12,
      assessment_id: 1,
      index: 1,
      description: "this is description",
      answered_value: 1,
      answers: {
        id: 123,
        assessment_id: 1,
        question_id: 12,
        label: "Social",
      },
      image: {
        src: "https://images.unsplash.com/photo-1556741533-6e6a62bd8b49?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cmVjZXB0aW9uaXN0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        alt: "Alt text",
      },
    },

    {
      id: 13,
      assessment_id: 1,
      index: 2,
      description: "this is description",

      answers: {
        id: 124,
        assessment_id: 1,
        question_id: 13,
        label: "Social",
      },
      image: {
        src: "https://images.unsplash.com/photo-1595751866979-de6e9d606220?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YmFydGVuZGVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        alt: "Alt text",
      },
    },
    {
      id: 14,
      assessment_id: 1,
      index: 3,
      description: "this is description",

      answers: {
        id: 125,
        assessment_id: 1,
        question_id: 14,
        label: "Social",
      },
      image: {
        src: "https://images.unsplash.com/photo-1556741533-6e6a62bd8b49?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cmVjZXB0aW9uaXN0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60",
        alt: "Alt text",
      },
    }
  ],
}


@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World!"}


@app.get("/api/v1/user/suggested-jobs" )
async def get_jobs():
    return mock_jobs

@app.get("/api/v1/user/work-motivation-test/assessment" )
async def get_jobs():
    return mock_work_motivation_test

