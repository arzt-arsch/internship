from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from db import engine, db_session
import models
import crud
import schemas

app: FastAPI = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = db_session()
    yield db


@app.post("/add_new_user/{pp}&{administrant}&{defendant}")
def add_new(pp: str, administrant: str, defendant: str, db: Session = Depends(get_db)):
    return crud.add_new_user(db, administrant, pp, defendant)


@app.get("/get_all_users")
def get_all(db: Session = Depends(get_db)):
    return crud.get_all_users(db)


@app.get("/get_user/{user_id}", response_model=schemas.MainTable)
def get_one(user_id: int, db: Session = Depends(get_db)):
    return crud.get_row_by_id(db, user_id)
