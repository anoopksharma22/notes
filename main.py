from fastapi import FastAPI,status
from apps.notes import routes as notes_routes
from db import SessionLocal, engine
from apps.users import (
    models as users_models, 
    schemas as users_schemas , 
    routes as users_routes)



app = FastAPI()

app.include_router(notes_routes.router)
app.include_router(users_routes.router)

@app.on_event("startup")
def create_tables():
    print("Creating tables")
    users_models.Base.metadata.create_all(bind=engine)

