from db import Base
from sqlalchemy import Column,ForeignKey,Boolean,DateTime,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from sqlalchemy.orm.session import Session
from apps.users.models import users as users_model
from apps.notes.models import notes as notes_model
from apps.notes.models import likes as likes_model
from fastapi import HTTPException,status
from sqlalchemy.exc import IntegrityError

class Likes(Base):
    __tablename__ = "likes"

    id = Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid.uuid4)
    note_id = Column(UUID(as_uuid=True),ForeignKey("notes.id"))
    user_id = Column(UUID(as_uuid=True),ForeignKey("users.id"))
    like = Column(Boolean,default=True)
    liked_ts = Column(DateTime,default=datetime.now())
    __table_args__ = (UniqueConstraint('note_id', 'user_id', name='uix_likes_1'),)

    ## relationships
    note = relationship("Notes",back_populates="like")
    user = relationship("Users",back_populates="like")


def like_a_post(db:Session,like:likes_model.Likes,user:users_model.Users):
    db_like = Likes(
        user_id = user.id,
        note_id = like.note_id,
        like = like.like
    )
    try:
        db.add(db_like)
        db.commit()
        db.refresh(db_like)
    except IntegrityError as ie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(ie.args))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e.args))
    
    return db_like


    