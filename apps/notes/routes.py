from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from . import models
from . import schemas
import db
from typing import List


router = APIRouter(
    prefix="/notes",
    tags=['notes']
)

@router.post("/",response_model=schemas.Note)
def create_note(note: schemas.CreateNote,db: Session = Depends(db.get_db)):
    note = models.create_note(db,note)
    return note

@router.get("/",response_model=List[schemas.Note])
def get_all_notes(db: Session = Depends(db.get_db)):
    note = models.get_all_notes(db)
    return note