from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db

router = APIRouter()

@router.get("/")
async def get_doctors(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    List doctors with pagination
    """
    return {"message": "List doctors", "skip": skip, "limit": limit}

@router.post("/")
async def create_doctor(db: Session = Depends(get_db)):
    """
    Create new doctor
    """
    return {"message": "Create doctor"}

@router.get("/{doctor_id}")
async def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    """
    Get doctor by ID
    """
    return {"message": f"Doctor {doctor_id}"}

@router.put("/{doctor_id}")
async def update_doctor(doctor_id: int, db: Session = Depends(get_db)):
    """
    Update doctor
    """
    return {"message": f"Update doctor {doctor_id}"}

@router.delete("/{doctor_id}")
async def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    """
    Delete doctor
    """
    return {"message": f"Delete doctor {doctor_id}"} 
