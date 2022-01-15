from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from .oauth2 import create_access_token,authenticate_user
import db

router = APIRouter(
    tags=['auth']
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(),db_session: Session = Depends(db.get_db)):

    user = authenticate_user(db_session,request.username,request.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")

    token = create_access_token(data={'sub':user.username})
    
    return {
       'access_token': token,
       'token_type': 'bearer',
       'user': user
    }