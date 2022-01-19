from uuid import UUID
from pydantic import BaseModel


class CreateLike(BaseModel):
    note_id: UUID
    like: bool

class Likes(CreateLike):
    id: UUID
    user_id: UUID

    class Config:
        orm_mode=True