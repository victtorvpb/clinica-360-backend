from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.api_v1.api import api_router

app = FastAPI(
    title="Clinica 360 API",
    description="""
    ## Medical Clinic Management System API
    
    Complete API for managing a medical clinic with the following features:
    
    ### Main Entities
    * **👤 Users**: Authentication and authorization system
    * **🏥 Patients**: Complete patient management with personal and medical data
    * **👨‍⚕️ Doctors**: Doctor management with specialties and CRM
    * **📅 Appointments**: Appointment scheduling and management
    
    ### Key Features
    * JWT Authentication
    * Role-based access control
    * Comprehensive CRUD operations
    * Advanced filtering and pagination
    * Real-time appointment status tracking
    
    ### Getting Started
    1. Register a new user or use demo credentials
    2. Authenticate to get access token
    3. Use the token in Authorization header: `Bearer <token>`
    """,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Clinica 360 API Support",
        "email": "support@clinica360.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Development server"
        },
        {
            "url": "https://api.clinica360.com",
            "description": "Production server"
        }
    ]
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

# Health check endpoint for Railway and monitoring
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for monitoring and deployment platforms."""
    return {"status": "healthy", "message": "Clinica 360 API is running!"}

# Define tags metadata for better Swagger organization
tags_metadata = [
    {
        "name": "Authentication",
        "description": "User authentication and authorization endpoints. Handle login, registration, and token management.",
        "externalDocs": {
            "description": "JWT Authentication Guide",
            "url": "https://jwt.io/introduction/",
        },
    },
    {
        "name": "Users",
        "description": "User management operations. Manage user accounts, profiles, and permissions.",
    },
    {
        "name": "Patients",
        "description": "Patient management operations. Complete CRUD operations for patient records including personal information, medical history, and contact details.",
    },
    {
        "name": "Doctors",
        "description": "Doctor management operations. Manage doctor profiles, specialties, CRM numbers, and availability.",
    },
    {
        "name": "Appointments",
        "description": "Appointment scheduling and management. Handle appointment booking, rescheduling, status updates, and medical records.",
    },
]

# Update FastAPI app with tags metadata
app.openapi_tags = tags_metadata

@app.get("/")
async def root():
    return {"message": "Clinica 360 API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 
