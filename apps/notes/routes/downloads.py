from fastapi import APIRouter,Depends
from apps.notes.schemas import downloads as downloads_schema
from apps.notes.models import downloads as downloads_model
from sqlalchemy.orm.session import Session
from apps.users.models import users as users_model
from apps.auth import oauth2
from db import get_db

router = APIRouter(
    prefix='/downloads',
    tags=['downloads','notes']
)

@router.post("/",response_model=downloads_schema.Download)
def download(download: downloads_schema.CreateDownload,db: Session = Depends(get_db),user: users_model.Users = Depends(oauth2.current_user_from_token)):
    comment = downloads_model.create_download(db,download,user)
    return comment