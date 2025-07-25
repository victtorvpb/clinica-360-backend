#!/usr/bin/env python3
"""
Script to initialize database with sample data
Run after executing migrations: python scripts/init_db.py
"""

import sys
import os

# Add root directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine
from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient, GenderEnum
from app.models.appointment import Appointment, AppointmentStatusEnum
from passlib.context import CryptContext
from datetime import datetime, date, timedelta

# Context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_sample_data():
    db: Session = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).first():
            print("❌ Data already exists in database. Skipping script...")
            return
        
        print("🏗️  Creating sample data...")
        
        # 1. Create admin user
        admin_user = User(
            email="admin@clinica360.com",
            name="System Administrator",
            hashed_password=pwd_context.hash("admin123"),
            is_active=True,
            is_superuser=True
        )
        db.add(admin_user)
        
        # 2. Create doctors
        doctors = [
            Doctor(
                name="Dr. João Silva",
                crm="12345-SP",
                specialty="Cardiologia",
                phone="(11) 99999-0001",
                email="joao.silva@clinica360.com",
                bio="Especialista em cardiologia com 15 anos de experiência."
            ),
            Doctor(
                name="Dra. Maria Santos",
                crm="67890-SP", 
                specialty="Dermatologia",
                phone="(11) 99999-0002",
                email="maria.santos@clinica360.com",
                bio="Dermatologista especializada em procedimentos estéticos."
            ),
            Doctor(
                name="Dr. Pedro Costa",
                crm="11111-SP",
                specialty="Clínico Geral",
                phone="(11) 99999-0003", 
                email="pedro.costa@clinica360.com",
                bio="Médico clínico geral com foco em medicina preventiva."
            )
        ]
        
        for doctor in doctors:
            db.add(doctor)
        
        # 3. Criar pacientes
        patients = [
            Patient(
                name="Ana Oliveira",
                cpf="12345678901",
                rg="123456789",
                birth_date=date(1985, 3, 15),
                gender=GenderEnum.feminino,
                phone="(11) 88888-0001",
                email="ana.oliveira@email.com",
                address="Rua das Flores, 123",
                city="São Paulo",
                state="SP",
                zip_code="01234-567",
                emergency_contact="Carlos Oliveira",
                emergency_phone="(11) 88888-0010"
            ),
            Patient(
                name="Carlos Mendes",
                cpf="23456789012", 
                rg="234567890",
                birth_date=date(1978, 7, 22),
                gender=GenderEnum.masculino,
                phone="(11) 88888-0002",
                email="carlos.mendes@email.com",
                address="Av. Paulista, 456",
                city="São Paulo", 
                state="SP",
                zip_code="01310-100",
                emergency_contact="Laura Mendes",
                emergency_phone="(11) 88888-0020"
            ),
            Patient(
                name="Beatriz Lima",
                cpf="34567890123",
                rg="345678901", 
                birth_date=date(1992, 11, 8),
                gender=GenderEnum.feminino,
                phone="(11) 88888-0003",
                email="beatriz.lima@email.com",
                address="Rua Augusta, 789",
                city="São Paulo",
                state="SP", 
                zip_code="01305-000",
                emergency_contact="José Lima",
                emergency_phone="(11) 88888-0030"
            )
        ]
        
        for patient in patients:
            db.add(patient)
            
        # Commit para ter IDs dos doctors e patients
        db.commit()
        
        # 4. Criar consultas
        appointments = [
            Appointment(
                patient_id=patients[0].id,
                doctor_id=doctors[0].id,
                appointment_date=datetime.now() + timedelta(days=1, hours=9),
                duration_minutes=30,
                status=AppointmentStatusEnum.agendada,
                reason="Consulta de rotina - cardiologia",
                price=150.00
            ),
            Appointment(
                patient_id=patients[1].id,
                doctor_id=doctors[1].id, 
                appointment_date=datetime.now() + timedelta(days=2, hours=14),
                duration_minutes=45,
                status=AppointmentStatusEnum.confirmada,
                reason="Avaliação dermatológica",
                price=200.00
            ),
            Appointment(
                patient_id=patients[2].id,
                doctor_id=doctors[2].id,
                appointment_date=datetime.now() + timedelta(days=3, hours=10, minutes=30),
                duration_minutes=30,
                status=AppointmentStatusEnum.agendada,
                reason="Check-up geral",
                price=120.00
            ),
            # Consulta passada - concluída
            Appointment(
                patient_id=patients[0].id,
                doctor_id=doctors[2].id,
                appointment_date=datetime.now() - timedelta(days=30),
                duration_minutes=30,
                status=AppointmentStatusEnum.concluida,
                reason="Consulta inicial",
                diagnosis="Paciente em bom estado geral",
                treatment="Manter atividade física regular",
                prescription="Vitamina D - 1000UI/dia",
                notes="Retorno em 6 meses",
                price=120.00
            )
        ]
        
        for appointment in appointments:
            db.add(appointment)
            
        db.commit()
        
        print("✅ Dados de exemplo criados com sucesso!")
        print("\n📋 Resumo:")
        print(f"   👤 Usuários: {db.query(User).count()}")
        print(f"   👨‍⚕️ Médicos: {db.query(Doctor).count()}")
        print(f"   🏥 Pacientes: {db.query(Patient).count()}")
        print(f"   📅 Consultas: {db.query(Appointment).count()}")
        
        print("\n🔑 Credenciais de acesso:")
        print("   Email: admin@clinica360.com")
        print("   Senha: admin123")
        
    except Exception as e:
        print(f"❌ Erro ao criar dados: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🚀 Inicializando banco de dados com dados de exemplo...")
    create_sample_data() 
