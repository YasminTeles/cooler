import uvicorn
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .database import engine, Base, SessionLocal
from . import crud
from .schemas import HistoryBase

app = FastAPI()


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
async def root():
    return {"message": "I'm working!"}


@app.post('/history/register', status_code=status.HTTP_201_CREATED)
def add_history(history: HistoryBase, session: Session = Depends(get_session)):
    if new_register := crud.add_register(session, history):
        return new_register

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("cooler.main:app", host="0.0.0.0", port=8000, reload=True)
