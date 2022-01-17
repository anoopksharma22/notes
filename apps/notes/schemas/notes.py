from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict,Optional
from apps.users.schemas import users as users_schema
from uuid import UUID
from typing import List,Dict,Any

class NoteBase(BaseModel):
    creates_ts: datetime
    updated_ts: datetime

class CreateNote(BaseModel):
    title: str
    content: Dict[Any, Any]    
    is_private: Optional[bool] = False
    tags: str


class Note(CreateNote):
    id: UUID
    user: users_schema.User


    class Config:
        orm_mode=True


