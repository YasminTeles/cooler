import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I'm working!"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("cooler.main:app", host="0.0.0.0", port=8000, reload=True)
