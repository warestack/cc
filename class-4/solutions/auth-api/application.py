from fastapi import FastAPI

import models
from database import engine
from routers import auth, profile


def create_app(db_engine=engine):
    models.Base.metadata.create_all(bind=db_engine)
    app = FastAPI()
    app.include_router(auth.router, prefix="/auth")
    app.include_router(profile.router, prefix="/profile")

    @app.get("/")
    def home():
        return {"message": "Week 4 auth API is running"}

    return app
