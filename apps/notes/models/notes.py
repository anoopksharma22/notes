import json
from turtle import st
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from apps import users
from db import Base
from sqlalchemy.orm.session import Session
from apps.notes.schemas import notes as notes_schema
from sqlalchemy.dialects.postgresql import JSON,UUID
import uuid
from fastapi import HTTPException,status

class Notes(Base):
        
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    title= Column(String)
    content = Column(JSON)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("Users",back_populates="note")



def create_note(db: Session, note: notes_schema.Note):
    note = Notes(
        user_id = note.user_id,
        title = note.title,
        content = note.content
    )
    try:
        db.add(note)
        db.commit()
        db.refresh(note)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return note


def get_all_notes(db:Session):
    notes = db.query(Notes).all()
    return notes