from sqlalchemy.orm import Session
import datetime
from models import MainTable


def get_row_by_id(db: Session, user_id: int):
    return db.query(MainTable).filter(MainTable.user_id == user_id).first()


def get_all_users(db: Session):
    return db.query(MainTable).all()


def add_new_user(db: Session, administrant: str, pp: str, defendant: str):
    db_user = MainTable(
        administrant=administrant,
        pp=pp,
        pp_date=datetime.datetime.now(),
        defendant=defendant,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
