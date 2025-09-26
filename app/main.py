from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users

app = FastAPI(
    title="Clinica 360 API",
    description="Backend API for Clinica 360 medical management system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Clinica 360 API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Clinica 360 API is running!",
        "timestamp": "2024-08-11T18:00:00Z"
    }

@app.get("/its-alive")
async def its_alive():
    """Simple alive check endpoint"""
    return {
        "message": "It's alive! 🧟‍♂️",
        "status": "alive"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
