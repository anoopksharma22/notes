from pydantic import BaseModel,Json
from typing import Any, Dict, List
from apps.users.schemas import users as users_schema
from uuid import UUID


class NoteBase(BaseModel):
    user_id: UUID
    title: str
    content: Dict[Any, Any]

class CreateNote(NoteBase):
    pass


class Note(NoteBase):
    id: UUID
    user: users_schema.User
    
    class Config:
        orm_mode=True


