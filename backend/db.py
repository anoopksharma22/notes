from turtle import circle
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

if config('ENV')== 'dev_local': 
    db_user=config('DB_USER')
    db_password=config('DB_PASSWORD')
    db_host=config('DB_HOST')
    db_port=config('DB_PORT')
    db_name=config('DB_NAME')
elif config('ENV')== 'dev_docker':
    db_user=config('DB_USER_DOCKER')
    db_password=config('DB_PASSWORD_DOCKER')
    db_host=config('DB_HOST_DOCKER')
    db_port=config('DB_PORT_DOCKER')
    db_name=config('DB_NAME_DOCKER')

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
