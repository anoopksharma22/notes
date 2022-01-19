from uuid import UUID
from pydantic import BaseModel


class CreateComment(BaseModel):
    note_id: UUID
    comment: str

class Comments(CreateComment):
    id: UUID
    user_id: UUID

    class Config:
        orm_mode=True