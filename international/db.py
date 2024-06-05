# from sqlmodel import  SQLModel



# sqlite_file_name = "data.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"



# def create_db_and_tables():
#     SQLModel.metadata.create_all(sqlite_url)

from sqlmodel import Field, SQLModel
from sqlmodel import create_engine, SQLModel



sqlite_file_name = "data.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)