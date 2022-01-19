from passlib.context import CryptContext
from sqlalchemy.orm.session import Session
import logging
logger = logging.getLogger(__name__)
component_logger = logger.getChild("component-a")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

