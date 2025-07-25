from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    """
    List users
    """
    return {"message": "List users"}

@router.get("/me")
async def get_current_user():
    """
    Get current user data
    """
    return {"message": "Current user"} 
