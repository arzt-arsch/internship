from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class MainTable(Base):
    __tablename__ = "main_table"
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    administrant = Column(String(50))
    pp = Column(String(50))
    pp_date = Column(Date())
    defendant = Column(String(50))
