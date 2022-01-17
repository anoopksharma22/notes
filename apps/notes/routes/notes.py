from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from apps.notes.models import notes as notes_model
from apps.notes.schemas import notes as notes_schema
from apps.users.models import users as users_model
from apps.auth import oauth2
import db
from typing import List

router = APIRouter(
    prefix="/notes",
    tags=['notes']
)

@router.post("/",response_model=notes_schema.Note)
def create_note(note:notes_schema.CreateNote,db: Session = Depends(db.get_db),user: users_model.Users = Depends(oauth2.current_user_from_token)):
    note = notes_model.create_note(db,note,user)
    return note

@router.get("/",response_model=List[notes_schema.Note])
def get_all_notes(db: Session = Depends(db.get_db)):
    note = notes_model.get_all_notes(db)
    return note