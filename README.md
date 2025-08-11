# Clinica 360 Backend

Backend API for **Clinica 360** medical management system built with **FastAPI**, **PostgreSQL** and **Poetry**.

## 🚀 Technologies

- **FastAPI** - Modern and fast web framework for Python
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for Python
- **Alembic** - Database migrations
- **Poetry** - Dependency management
- **Pydantic** - Data validation

## 📁 Project Structure

```
clinica-360-backend/
├── app/
│   ├── api/                 # API endpoints
│   ├── core/               # Core configurations
│   ├── db/                 # Database configuration
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   └── main.py             # Main FastAPI application
├── pyproject.toml          # Poetry configuration
└── README.md
```

## 🛠️ Setup and Installation

### Option 1: Docker (Recommended)

#### Prerequisites
- Docker and Docker Compose
- Make (optional, for convenience)

#### Quick Start with Docker

```bash
# Build and start all services
make build
make up

# OR use docker-compose directly
docker-compose up -d

# View logs
make logs
# OR
docker-compose logs -f

# Test the API
make test
```

#### Docker Services
- **API**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **pgAdmin**: http://localhost:5050 (admin@clinica360.com / admin123)

### Option 2: Local Development

#### Prerequisites
- Python 3.12+
- Poetry
- PostgreSQL (for production)

#### 1. Install Dependencies

```bash
# Install dependencies using Poetry
poetry install
```

#### 2. Run the Application

```bash
# Run with Poetry
poetry run python app/main.py

# OR run with uvicorn directly
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Access the API

- **API Documentation**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **Alive Check**: http://localhost:8000/its-alive

## 🏥 Features

### Current Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /its-alive` - Simple alive check

### Planned Features

- **👤 Users**: Authentication and authorization system
- **🏥 Patients**: Complete patient management
- **👨‍⚕️ Doctors**: Doctor management with specialties
- **📅 Appointments**: Appointment scheduling and management

## 🧪 Development

### Docker Commands

```bash
# View available commands
make help

# Start development environment
make dev

# View logs
make logs

# Access API container shell
make shell

# Test API endpoints
make test

# Restart services
make restart

# Clean up everything
make clean
```

### Local Development

```bash
# Run in development mode with auto-reload
poetry run uvicorn app.main:app --reload

# Run tests (when implemented)
poetry run pytest

# Format code (when implemented)
poetry run black .
```

### Database Management

```bash
# Access PostgreSQL shell
make db-shell

# Backup database
make db-backup

# Restore database
make db-restore FILE=backup_file.sql
```

## 📝 License

MIT License
