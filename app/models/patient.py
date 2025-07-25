from sqlalchemy import Column, Integer, String, Date, Enum, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from app.db.database import Base

class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    cpf = Column(String(11), unique=True, nullable=False, index=True)
    rg = Column(String(20), nullable=True)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    phone = Column(String(20), nullable=True)
    email = Column(String, nullable=True)
    address = Column(Text, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String(2), nullable=True)
    zip_code = Column(String(10), nullable=True)
    emergency_contact = Column(String, nullable=True)
    emergency_phone = Column(String(20), nullable=True)
    medical_notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    appointments = relationship("Appointment", back_populates="patient") 
