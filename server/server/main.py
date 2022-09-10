from fastapi import FastAPI

app = FastAPI(title="CodeToGive backend server")

@app.get("/")
async def root():
    return {"message": "Hello World!"}
    
