from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from . import crud
from .database import get_session, create_database
from .schemas import HistoryBase

itemrouter = APIRouter()
create_database()


@itemrouter.get("/")
async def root():
    return {"message": "I'm working!"}


@itemrouter.post('/history/register', status_code=status.HTTP_201_CREATED)
def add_history(history: HistoryBase, session: Session = Depends(get_session)):
    if new_register := crud.add_register(session, history):
        return new_register

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
