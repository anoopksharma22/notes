import uuid
from fastapi import APIRouter,Depends
from apps.notes.schemas import likes as likes_schema
from apps.notes.models import likes as likes_model
from sqlalchemy.orm.session import Session
from apps.users.models import users as users_model
from apps.auth import oauth2
from db import get_db
from typing import List

router = APIRouter(
    prefix='/likes',
    tags=['likes']
)

@router.post("/",response_model=likes_schema.Likes)
def create_like(like: likes_schema.CreateLike,db: Session = Depends(get_db),user: users_model.Users = Depends(oauth2.current_user_from_token)):
    like = likes_model.like_a_post(db,like,user)
    return like