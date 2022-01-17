from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from apps import users
from db import Base
from sqlalchemy.orm.session import Session
from apps.notes.schemas import notes as notes_schema
from sqlalchemy.dialects.postgresql import JSON,UUID
import uuid
from datetime import datetime
from apps.users.schemas import users as users_schema

class Notes(Base):
        
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    title= Column(String)
    content = Column(JSON)
    is_private = Column(Boolean,default=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    tags = Column(String)
    created_ts = Column(DateTime,default=datetime.now())
    updated_ts = Column(DateTime,default=datetime.now())
    
    user = relationship("Users",back_populates="note")
    like = relationship("Likes",back_populates="note")     
    comment = relationship("Comments",back_populates="note")
    download = relationship("Downloads",back_populates="note")


def create_note(db: Session, note: notes_schema.Note, user: users_schema.User):
    db_note = Notes(
        user_id = user.id,
        title = note.title,
        content = note.content,
        is_private = note.is_private,
        tags = note.tags
    )
    
    db.add(db_note)   
    db.commit()
    db.refresh(db_note)    
    return db_note


def get_all_notes(db:Session):
    notes = db.query(Notes).all()
    return notes