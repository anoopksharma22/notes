from pydantic import BaseModel,Json
from typing import Any, Dict, List
from apps.users.schemas import User
from uuid import UUID


class NoteBase(BaseModel):
    user_id: UUID
    title: str
    content: Dict[Any, Any]

class CreateNote(NoteBase):
    pass


class Note(NoteBase):
    id: UUID
    user: User
    
    class Config:
        orm_mode=True


