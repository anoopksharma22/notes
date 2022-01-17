from sqlalchemy import Column,ForeignKey,UniqueConstraint,String,DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from db import Base
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,status

class Comments(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid4)
    note_id = Column(UUID(as_uuid=True),ForeignKey("notes.id"))
    user_id = Column(UUID(as_uuid=True),ForeignKey("users.id"))
    comment = Column(String)
    comment_ts = Column(DateTime,default=datetime.now())

    user = relationship("Users",back_populates="comment")
    note = relationship("Notes",back_populates="comment")


def create_comment(db,comment,user):
    db_comment = Comments(
        user_id = user.id,
        note_id = comment.note_id,
        comment = comment.comment
    )
    try:
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
    except IntegrityError as ie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(ie.args))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e.args))
    
    return db_comment