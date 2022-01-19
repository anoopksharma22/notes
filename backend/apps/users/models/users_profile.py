from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.dialects.postgresql import UUID,JSON
import uuid

class UsersProfile(Base):
    
    __tablename__ = "users_profile"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    social = Column(JSON)
    profile_picture = Column(String)
    user = relationship("Users",back_populates="user_profile")