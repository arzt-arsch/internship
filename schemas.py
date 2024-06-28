from pydantic import BaseModel
from datetime import datetime


class MainTable(BaseModel):
    user_id: int
    administrant: str
    pp: str
    pp_date: datetime
    defendant: str

    class Config:
        orm_mode = True
