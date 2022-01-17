from sqlalchemy import Column,ForeignKey,UniqueConstraint,String,DateTime,Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from db import Base

class Downloads(Base):
    __tablename__ = "downloads"

    id = Column(UUID(as_uuid=True),primary_key=True,index=True,default=uuid4)
    note_id = Column(UUID(as_uuid=True),ForeignKey("notes.id"))
    user_id = Column(UUID(as_uuid=True),ForeignKey("users.id"))
    no_of_downloads = Column(Integer)
    download_ts = Column(DateTime,default=datetime.now())

    user = relationship("Users",back_populates="download")
    note = relationship("Notes",back_populates="download")


def create_download(db,download,user):
    
    db_download = db.query(Downloads).filter(Downloads.user_id==user.id).filter(Downloads.note_id==download.note_id).first()
    
    
    if db_download:
        db_download.no_of_downloads += 1
        db_download.download_ts = datetime.now()
        db.commit()
        db.refresh(db_download)
        return db_download
    
   
    new_download = Downloads(
        user_id = user.id,
        note_id = download.note_id,
        no_of_downloads = 1
    )
    db.add(new_download)
    db.commit()
    db.refresh(new_download)
    return new_download