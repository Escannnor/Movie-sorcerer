from sqlmodel import Field, SQLModel
from db import create_db_and_tables
from sqlmodel import UniqueConstraint

class Kdrama(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    name : str 
    date : str 
    description : str
    image_link : str
    url : str
    __table_args__ = (UniqueConstraint('name', 'date'),)


create_db_and_tables()