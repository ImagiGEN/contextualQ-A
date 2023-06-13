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

class FetchTranscript(BaseModel):
    company_name: str
    year: int
    quarter: int
    api_key: str
    openai_api_key: str
    word_limit: int

class QueryTranscript(BaseModel):
    query: str
    openai_api_key: str
    api_key: str
    word_limit: int
    embedding: str