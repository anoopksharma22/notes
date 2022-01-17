from uuid import UUID
from pydantic import BaseModel


class CreateDownload(BaseModel):
    note_id: UUID

class Download(CreateDownload):
    id: UUID
    user_id: UUID
    no_of_downloads: int

    class Config:
        orm_mode=True