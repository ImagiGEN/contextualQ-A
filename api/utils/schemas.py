from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    cnf_password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class CompanyMetadata(BaseModel):
    company_names_years: dict
