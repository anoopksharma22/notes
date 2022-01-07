from fastapi import APIRouter,HTTPException,status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from typing import List
from db import get_db
from . import crud
from . import schemas

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = crud.get_users_by_email(db,user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="email already used")
    db_user = crud.create_user(db,user)
    return db_user

@router.get("/", response_model=List[schemas.User])
def get_all_user(db: Session = Depends(get_db)):
    db_users = crud.get_all_users(db)
    if not db_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Users not found")    
    return db_users

@router.get("/{id}", response_model=schemas.User)
def get_all_user(db: Session = Depends(get_db), id:int=id):
    db_user = crud.get_user_by_id(db,id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Users not found")    
    return db_user


@router.delete("/{id}")
def get_all_user(db: Session = Depends(get_db),id:int = id):
    db_users = crud.get_user_by_id(db,id)
    print(db_users)
    if not db_users:
        print("User not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Users not found")    
    crud.delete_user(db,id)
    return {}