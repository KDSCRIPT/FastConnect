from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg.rows import dict_row
from app.config import settings


SQLALCHEMY_DATABASE_URL=f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine=create_engine(SQLALCHEMY_DATABASE_URL,echo=True)
SessionLocal=sessionmaker(autoflush=False,bind=engine)
Base=declarative_base()


#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#postgres driver code
# try:
#     conn=psycopg.connect("host=localhost dbname=fastapi user=postgres password=Acdnfmabjjbads1",row_factory=dict_row)
#     cursor=conn.cursor()
#     print("Database connection was successful!")
# except Exception as error:
#     print("Connecting to database failed")
#     print("Error:",error)
#     raise error