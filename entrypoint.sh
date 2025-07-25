#!/bin/bash

# Exit on any error
set -e

echo "🔄 Starting Clinica 360 API..."

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
while ! pg_isready -h $POSTGRES_SERVER -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 2
done

echo "✅ PostgreSQL is ready!"

# Run database migrations
echo "🔄 Running database migrations..."
alembic upgrade head

echo "✅ Migrations completed!"

# Start the FastAPI application
echo "🚀 Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 
