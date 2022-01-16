from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt,JWTError
from fastapi import HTTPException,status,Depends
from sqlalchemy.orm.session import Session
from passlib.context import CryptContext
import db
from ..users import models as user_model
     
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
SECRET_KEY = '43eb241ae521e2cc7477b691fdd1f3ce8221d90f1437fcd03bd0cce801799e4e'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1
    
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def current_user_from_token(token: str = Depends(oauth2_scheme),db_session: Session = Depends(db.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
    user = user_model.get_users_by_username(db=db_session, username=username)
    if user is None:
        raise credentials_exception
    return user



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db_session: Session,username: str , password: str):
    user = user_model.get_users_by_username(db=db_session, username=username)
    print(user)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user