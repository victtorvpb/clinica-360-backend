from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.post("/login")
async def login(db: Session = Depends(get_db)):
    """
    Login endpoint - implement JWT authentication
    """
    return {"message": "Login endpoint - implement JWT"}

@router.post("/register")
async def register(db: Session = Depends(get_db)):
    """
    User registration endpoint
    """
    return {"message": "Register endpoint - implement user creation"} 
