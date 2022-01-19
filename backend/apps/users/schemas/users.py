from typing import Optional
from pydantic import BaseModel
from sqlalchemy import orm
from uuid import UUID
from apps.users.schemas import users_profile as users_profile_schema

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
    user_profile: users_profile_schema.UsersProfile
    
    class Config:
        orm_mode=True



class UsersProfile(BaseModel):
    id:UUID
    user_id:UUID
    
    class Config:
        orm_mode=True