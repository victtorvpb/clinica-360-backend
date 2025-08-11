.PHONY: help build up down logs shell clean test migrate migrate-create migrate-upgrade migrate-downgrade

# Default target
help:
	@echo "Clinica 360 Backend - Available commands:"
	@echo ""
	@echo "  build    - Build Docker images"
	@echo "  up       - Start all services"
	@echo "  down     - Stop all services"
	@echo "  logs     - Show logs from all services"
	@echo "  api-logs - Show logs from API service only"
	@echo "  shell    - Open shell in API container"
	@echo "  clean    - Remove containers, networks, and volumes"
	@echo "  test     - Test the API endpoints"
	@echo "  restart  - Restart all services"
	@echo ""
	@echo "Migration commands:"
	@echo "  migrate-create MESSAGE='desc' - Create new migration"
	@echo "  migrate-upgrade              - Apply pending migrations"
	@echo "  migrate-downgrade            - Rollback last migration"

# Build Docker images
build:
	docker-compose build

# Start all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# Show logs from all services
logs:
	docker-compose logs -f

# Show logs from API service only
api-logs:
	docker-compose logs -f api

# Open shell in API container
shell:
	docker-compose exec api bash

# Remove containers, networks, and volumes
clean:
	docker-compose down -v --remove-orphans
	docker system prune -f

# Test the API endpoints
test:
	@echo "Testing API endpoints..."
	@echo "Health check:"
	@curl -s http://localhost:8000/health | jq .
	@echo ""
	@echo "Alive check:"
	@curl -s http://localhost:8000/its-alive | jq .
	@echo ""
	@echo "Root endpoint:"
	@curl -s http://localhost:8000/ | jq .

# Restart all services
restart:
	docker-compose restart

# Development mode with hot reload
dev:
	docker-compose up

# Production mode
prod:
	docker-compose -f docker-compose.yml up -d

# Database commands
db-shell:
	docker-compose exec db psql -U clinica360 -d clinica360

# Backup database
db-backup:
	docker-compose exec db pg_dump -U clinica360 clinica360 > backup_$(shell date +%Y%m%d_%H%M%S).sql

# Restore database
db-restore:
	@echo "Usage: make db-restore FILE=backup_file.sql"
	@if [ -z "$(FILE)" ]; then echo "Please specify FILE parameter"; exit 1; fi
	docker-compose exec -T db psql -U clinica360 -d clinica360 < $(FILE)

# Migration commands
migrate:
	@echo "Available migration commands:"
	@echo "  make migrate-create MESSAGE='description' - Create new migration"
	@echo "  make migrate-upgrade                     - Apply all pending migrations"
	@echo "  make migrate-downgrade                   - Rollback last migration"

migrate-create:
	@if [ -z "$(MESSAGE)" ]; then echo "Please specify MESSAGE parameter"; exit 1; fi
	docker-compose exec api alembic revision --autogenerate -m "$(MESSAGE)"

migrate-upgrade:
	docker-compose exec api alembic upgrade head

migrate-downgrade:
	docker-compose exec api alembic downgrade -1
