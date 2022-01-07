from typing import Optional
from pydantic import BaseModel
from sqlalchemy import orm



class UserBase(BaseModel):
    email:str


class CreateUser(UserBase):
    name:Optional[str]
    usrname:str
    password:str

class User(UserBase):
    id:int
    name:Optional[str]
    username:str    
    is_verified:Optional[bool] = False
    is_active:Optional[bool] = False
    
    class Config:
        orm_mode=True