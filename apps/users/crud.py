
from sqlalchemy.orm import Session
from .models import Users
from .schemas import CreateUser, User



def create_user(db:Session, user: CreateUser):    
    db_user = Users(
        name = user.name,
        username=user.usrname,
        email=user.email,
        password = user.password,        
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db:Session):
    return db.query(Users).all()

def get_users_by_username(db:Session,username:str):
    return db.query(Users).filter(Users.username == username)

def get_user_by_id(db:Session,user_id:int):
    return db.query(Users).filter(Users.id == user_id).first()

def get_users_by_email(db:Session ,email: str):
    return db.query(Users).filter(Users.email == email).first()

def update_user():
    pass

def delete_user(db:Session,id:int):    
    db.query(Users).filter(Users.id == id).delete()
    db.commit()