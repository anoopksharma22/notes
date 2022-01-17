from fastapi import FastAPI,status
from apps.notes.routes import (
    notes as notes_routes,
    likes as likes_routes)
from apps.users.models import (
    users as users_models,
    users_profile as users_profile_model)
from db import SessionLocal, engine
from apps.users.routes import users as users_routes
from apps.notes.models import notes as notes_models
from apps.notes.models import likes as likes_model

from apps.auth import routes as auth_routes
import logging
from decouple import config

# logging.basicConfig(level=logging.NOTSET) ## to reset the root looging level
logger = logging.getLogger(__name__)
env = config('ENV')

if env == 'dev_local':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARNING)

app = FastAPI()

logging.info('Setting up routes')
app.include_router(notes_routes.router)
app.include_router(users_routes.router)
app.include_router(auth_routes.router)
app.include_router(likes_routes.router)

@app.on_event("startup")
def create_tables():
    logger.info("Creating tables")
    users_models.Base.metadata.create_all(bind=engine)
    notes_models.Base.metadata.create_all(bind=engine)
    users_profile_model.Base.metadata.create_all(bind=engine)
    likes_model.Base.metadata.create_all(bind=engine)    
    
    

