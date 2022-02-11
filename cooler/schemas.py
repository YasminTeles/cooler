from pydantic import BaseModel


class HistoryBase(BaseModel):
    type_beverage: str
    amount: int
    movement: str
