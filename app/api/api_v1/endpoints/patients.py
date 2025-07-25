from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db

router = APIRouter()

@router.get("/")
async def get_patients(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    List patients with pagination
    """
    return {"message": "List patients", "skip": skip, "limit": limit}

@router.post("/")
async def create_patient(db: Session = Depends(get_db)):
    """
    Create new patient
    """
    return {"message": "Create patient"}

@router.get("/{patient_id}")
async def get_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Get patient by ID
    """
    return {"message": f"Patient {patient_id}"}

@router.put("/{patient_id}")
async def update_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Update patient
    """
    return {"message": f"Update patient {patient_id}"}

@router.delete("/{patient_id}")
async def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Delete patient
    """
    return {"message": f"Delete patient {patient_id}"} 
