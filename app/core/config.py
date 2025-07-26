from typing import List, Optional
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Clinica 360"
    
    # Database - Railway auto-provides DATABASE_URL
    DATABASE_URL: Optional[str] = None
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "clinica_user"
    POSTGRES_PASSWORD: str = "clinica_password"
    POSTGRES_DB: str = "clinica_360"
    POSTGRES_PORT: str = "5432"
    
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        # Use DATABASE_URL from Railway if available
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    # CORS - simplified for now
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "*"]
    
    # Security
    SECRET_KEY: str = "clinica-360-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    ALGORITHM: str = "HS256"
    
    # Development
    DEBUG: bool = True
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # Production settings
    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT.lower() == "production"
    
    class Config:
        case_sensitive = True

settings = Settings() 
