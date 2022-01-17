from typing import Optional
from pydantic import BaseModel
from sqlalchemy import orm
from uuid import UUID
from typing import Dict,Any

class UsersProfile(BaseModel):
    id:UUID
    user_id:UUID
    social: Optional[Dict[Any, Any]]
    profile_picture:Optional[str]

    class Config:
        orm_mode=True