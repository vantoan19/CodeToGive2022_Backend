from fastapi import FastAPI

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")

@app.get("/api/v1/hello")
async def root():
    return {"message": "Hello World!"}
    
