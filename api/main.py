
from fastapi import FastAPI
from sqlalchemy.orm import relationship
from database import models, engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Transcript Insight")


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/health")
async def check() -> dict:
    return {"message": "OK"}


@app.get("/api/v1/user/register")
async def register_user() -> dict:
    return {"message": "User registered successfully"}
