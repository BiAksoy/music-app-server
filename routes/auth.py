import uuid
import bcrypt
from fastapi import Depends, HTTPException
import jwt
from config import JWT_SECRET_KEY
from middleware.auth_middleware import auth_middleware
from models.user import User
from fastapi import APIRouter
from database import get_db
from sqlalchemy.orm import Session, joinedload

from pydantic_schemas.user_create import UserCreate
from pydantic_schemas.user_login import UserLogin

router = APIRouter()

@router.post('/signup')
def signup_user(user: UserCreate, db: Session=Depends(get_db)):
    # Check if user already exists
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(status_code=400, detail='User already exists')
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password= hashed_pw
    )

    # Save user to database
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

@router.post('/login')
def login_user(user: UserLogin, db: Session=Depends(get_db)):
    # Check if user exists
    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        raise HTTPException(status_code=400, detail='User not found')
    
    # Check if password is correct
    if not bcrypt.checkpw(user.password.encode(), user_db.password):
        raise HTTPException(status_code=400, detail='Invalid password')
    
    token = jwt.encode({'user_id': user_db.id}, JWT_SECRET_KEY)
    
    return {'token': token, 'user': user_db}

@router.get('/')
def get_current_user(db: Session=Depends(get_db), user_dict=Depends(auth_middleware)):
    user = db.query(User).filter(User.id == user_dict['user_id']).options(
        joinedload(User.favorites)
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user
    