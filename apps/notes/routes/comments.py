from fastapi import APIRouter,Depends
from apps.notes.schemas import comments as comments_schema
from apps.notes.models import comments as comments_model
from sqlalchemy.orm.session import Session
from apps.users.models import users as users_model
from apps.auth import oauth2
from db import get_db

router = APIRouter(
    prefix='/comments',
    tags=['comments','notes']
)

@router.post("/",response_model=comments_schema.Comments)
def create_like(comment: comments_schema.CreateComment,db: Session = Depends(get_db),user: users_model.Users = Depends(oauth2.current_user_from_token)):
    comment = comments_model.create_comment(db,comment,user)
    return comment