from sqlalchemy.orm import Session  # type: ignore

from .schemas import HistoryBase
from .models import History

def add_register(session: Session, history: HistoryBase):
    new_register = History(**history.dict())

    session.add(new_register)
    session.commit()
    session.refresh(new_register)

    return new_register
