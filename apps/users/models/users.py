import imp
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from db import Base
from ...auth import password
from apps.users.schemas import users as users_schema
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Users(Base):
    
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_verfied = Column(Boolean, default=False) 
    is_active = Column(Boolean, default=False)
    note = relationship("Notes",back_populates="user")





def create_user(db:Session, user: users_schema.CreateUser):
    hashed_password = password.get_password_hash(user.password)
    db_user = Users(
        name = user.name,
        username=user.username,
        email=user.email,
        password = hashed_password,        
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db:Session):
    return db.query(Users).all()


def get_users_by_username(db:Session,username:str):
    return db.query(Users).filter(Users.username == username).first()

def get_user_by_id(db:Session,user_id:int):
    return db.query(Users).filter(Users.id == user_id).first()

def get_users_by_email(db:Session ,email: str):
    return db.query(Users).filter(Users.email == email).first()

def update_user():
    pass

def delete_user(db:Session,id:int):    
    db.query(Users).filter(Users.id == id).delete()
    db.commit()


def authenticate_user(db_session: Session,username: str , password: str):
    user = get_users_by_username(db_session=db_session, username=username)
    print("got user as :" + user)
    if not user:
        return False
    if not password.verify_password(password, user.password):
        return False
    return user