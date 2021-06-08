from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    email: str
    password: str
    is_active: bool
