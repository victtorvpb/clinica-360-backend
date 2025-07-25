#!/usr/bin/env python3
"""
Setup script for Clinica 360 Backend
Run: python scripts/setup.py
"""

import os
import shutil
import sys

def setup_project():
    """Setup the project with basic configuration"""
    print("🚀 Setting up Clinica 360 Backend...")
    
    # Check if we're in the right directory
    if not os.path.exists("app/main.py"):
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    # Create .env file if it doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists("env.example"):
            shutil.copy("env.example", ".env")
            print("✅ Created .env file from env.example")
        else:
            print("❌ env.example file not found")
            sys.exit(1)
    else:
        print("⚠️  .env file already exists, skipping...")
    
    # Create necessary directories
    dirs_to_create = [
        "logs",
        "uploads",
        "data"
    ]
    
    for directory in dirs_to_create:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created {directory}/ directory")
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your settings")
    print("2. Run: docker-compose up -d")
    print("3. Run: docker-compose exec api alembic upgrade head")
    print("4. Run: docker-compose exec api python scripts/init_db.py")
    print("\n🌐 Access:")
    print("- API: http://localhost:8000")
    print("- Docs: http://localhost:8000/docs")

if __name__ == "__main__":
    setup_project() 
