
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from utils import models, engine, SessionLocal, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Transcript Insight")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/health")
async def check() -> dict:
    return {"message": "OK"}


@app.post("/api/v1/user/register", response_model=schemas.User)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if not (user.username and
            user.password and
            user.cnf_password):
        raise HTTPException(
            status_code=404, detail=r"Username and password cannot be empty")
    if user.password != user.cnf_password:
        raise HTTPException(
            status_code=404, detail=r"Provided passwords do not match")
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
