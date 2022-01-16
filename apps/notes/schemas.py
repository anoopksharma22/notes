from pydantic import BaseModel

from apps.users.schemas import User

class NoteBase(BaseModel):
    user_id: int
    title: str
    content: str


class CreateNote(NoteBase):
    pass


class Note(NoteBase):
    id: int
    user: User
    
    class Config:
        orm_mode=True

