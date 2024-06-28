from sqlalchemy import Table, Column, Integer, String, Date, MetaData, create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(
    "sqlite:///./db.sqlite", connect_args={"check_same_thread": False}
)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
