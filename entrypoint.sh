#!/bin/bash

# Exit on any error
set -e

echo "🔄 Starting Clinica 360 API..."

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."

# If using DATABASE_URL, extract connection details
if [ ! -z "$DATABASE_URL" ]; then
  echo "Using DATABASE_URL for connection"
  # Extract host and port from DATABASE_URL for pg_isready
  DB_HOST=$(echo $DATABASE_URL | sed -n 's/.*@\([^:]*\):.*/\1/p')
  DB_PORT=$(echo $DATABASE_URL | sed -n 's/.*:\([0-9]*\)\/.*/\1/p')
  DB_USER=$(echo $DATABASE_URL | sed -n 's/.*\/\/\([^:]*\):.*/\1/p')
  
  while ! pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 2
  done
else
  # Use environment variables
  while ! pg_isready -h $POSTGRES_SERVER -p $POSTGRES_PORT -U $POSTGRES_USER; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 2
  done
fi

echo "✅ PostgreSQL is ready!"

# Run database migrations
echo "🔄 Running database migrations..."
alembic upgrade head

echo "✅ Migrations completed!"

# Start the FastAPI application
echo "🚀 Starting FastAPI application..."

# Use PORT from Railway if available, default to 8000
PORT=${PORT:-8000}

# Disable reload in production
if [ "$ENVIRONMENT" = "production" ]; then
    echo "🏭 Starting in production mode (no reload)"
    exec uvicorn app.main:app --host 0.0.0.0 --port $PORT
else
    echo "🔧 Starting in development mode (with reload)"
    exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload
fi 
