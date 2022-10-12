import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#SQLALCHEMY_DATABASE_URL = 'sqlite:///./chefofceylon_api.db' #os.environ['SQLALCHEMY_DATABASE_URL']
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root@localhost:3306/chef_api' #os.environ['SQLALCHEMY_DATABASE_URL']
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def init_db(app: FastAPI) -> None:
    Base.metadata.create_all(engine)
