from typing import Optional
from pydantic import BaseModel
from sqlalchemy import orm
from uuid import UUID


class UserBase(BaseModel):
    email:str


class CreateUser(UserBase):
    name:Optional[str]
    username:str
    password:str

class User(UserBase):
    id:UUID
    name:Optional[str]
    username:str    
    is_verified:Optional[bool] = False
    is_active:Optional[bool] = False
    
    class Config:
        orm_mode=True