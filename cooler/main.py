import uvicorn
from fastapi import FastAPI

from .routers import itemrouter

app = FastAPI()
app.include_router(itemrouter)

def start():
    uvicorn.run("cooler.main:app", host="0.0.0.0", port=8000, reload=True)
