from sqlalchemy.orm import Session
from utils import models, schemas, common


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def validate_user(db: Session, user: schemas.UserCreate):
    hashed_password = common.get_hashed_password(user.password).decode('utf-8')
    return db.query(models.User).filter(models.User.username == user.username and models.User.hashed_password == hashed_password).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def validate_access_token(db: Session, access_token: str):
    decoded_data = common.decode_token(access_token)
    common.compare_time(decoded_data["exp"])
    username = decoded_data["username"]
    hashed_password = decoded_data["password"]
    return db.query(models.User).filter(
        models.User.username == username and
        models.User.hashed_password == hashed_password).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = common.get_hashed_password(user.password).decode('utf-8')
    db_user = models.User(username=user.username,
                          hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def metadata_fetch_company_years(db: Session, skip: int = 0, limit: int = 100):
    db_metadata = db.query(models.CompanyMetadata).offset(skip).limit(limit).all()
    return db_metadata

def store_company_metadata(db: Session, metadata: schemas.CompanyMetadata):
    for data in metadata.list:
        print(data)
        for year in data[1]:
            d = models.CompanyMetadata(name=data[0],
                                       year=year)
            db.add(d)
    db.commit()
    return True