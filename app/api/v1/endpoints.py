import hashlib

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.user import User
from app.schemas.user_schema import UserResponseSchema, UserSchema

router = APIRouter()


@router.get("/user/{uid}", response_model=UserResponseSchema)
def get_user(uid: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == uid).one()
    return user


@router.post("/user")
def create_user(req: UserSchema, db: Session = Depends(get_db)):
    hashed_password = hashlib.sha256(req.password.encode()).hexdigest()
    db_user = User(
        email=req.email, hashed_password=hashed_password, is_active=req.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.id
