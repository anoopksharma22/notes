from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from apps import users
from db import Base
from sqlalchemy.orm.session import Session
from . import schemas


class Notes(Base):
        
    __tablename__ = "Notes"

    id = Column(Integer, primary_key=True, index=True)
    title= Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship("Users",back_populates="notes")



def create_note(db: Session, note: schemas.Note):
    note = Notes(
        user_id = note.user_id,
        title = note.title,
        content = note.content
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_all_notes(db:Session):
    notes = db.query(Notes).all()
    return notes