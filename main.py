from fastapi import FastAPI,status
from apps.notes import routes as notes_routes
from db import SessionLocal, engine
from apps.users import (
    models as users_models, 
    schemas as users_schemas , 
    routes as users_routes)
from apps.auth import routes as auth_routes
import logging
from config import Settings
settings = Settings()

# logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
log_level = settings.getLogLevel()
print("###########################")
print(log_level.DEV)
# logger.setLevel(log_level.DEV)

app = FastAPI()

logging.info('Setting up routes')
app.include_router(notes_routes.router)
app.include_router(users_routes.router)
app.include_router(auth_routes.router)

@app.on_event("startup")
def create_tables():
    logger.info("Creating tables")
    users_models.Base.metadata.create_all(bind=engine)

