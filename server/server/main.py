from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from server.api.v1.apiv1 import apiv1_router
from server.crud import NotImplementedException

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")


@app.exception_handler(NotImplementedException)
async def crud_not_implemented_exception_handler(
    request: Request, exc: NotImplementedException
):
    return JSONResponse(
        status_code=501,
        content={
            "detail": f"The CRUD component {exc.crud_component} does not implement operation {exc.crud_operation}"
        },
    )


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apiv1_router, prefix="/api/v1")
