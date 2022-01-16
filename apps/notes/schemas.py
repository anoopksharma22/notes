import json

from pydantic import BaseModel,Json
from typing import Dict, List

from apps.users.schemas import User

class Comment(BaseModel):
    msg: str


class NoteBase(BaseModel):
    user_id: int
    title: str
    content: Comment

class CreateNote(NoteBase):
    pass


class Note(NoteBase):
    id: int
    user: User
    
    class Config:
        orm_mode=True


