import json

from pydantic import BaseModel,Json
from typing import Any, Dict, List

from apps.users.schemas import User


class NoteBase(BaseModel):
    user_id: int
    title: str
    content: Dict[Any, Any]

class CreateNote(NoteBase):
    pass


class Note(NoteBase):
    id: int
    user: User
    
    class Config:
        orm_mode=True


