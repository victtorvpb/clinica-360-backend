from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.post("/login", summary="User Login", tags=["Authentication"])
async def login(db: Session = Depends(get_db)):
    """
    ## User Login
    
    Authenticate user and return JWT access token.
    
    **Request Body:**
    - `email`: User email address
    - `password`: User password
    
    **Response:**
    - `access_token`: JWT token for authentication
    - `token_type`: Always "bearer"
    - `expires_in`: Token expiration time in seconds
    
    **Example:**
    ```json
    {
        "email": "admin@clinica360.com",
        "password": "admin123"
    }
    ```
    """
    return {"message": "Login endpoint - implement JWT"}

@router.post("/register")
async def register(db: Session = Depends(get_db)):
    """
    User registration endpoint
    """
    return {"message": "Register endpoint - implement user creation"} 
