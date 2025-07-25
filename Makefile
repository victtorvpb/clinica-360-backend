# Clinica 360 Backend - Makefile
# Quick commands for development

.PHONY: help setup up down logs clean swagger test migrate init-db

help: ## Show this help message
	@echo "Clinica 360 Backend Commands:"
	@echo "=============================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Setup project (create .env, directories)
	@python scripts/setup.py

up: ## Start all services with Docker Compose
	@echo "🚀 Starting Clinica 360 Backend..."
	@docker-compose up -d
	@echo "✅ Services started!"
	@echo "🌐 API: http://localhost:8000"
	@echo "📚 Swagger: http://localhost:8000/docs"

down: ## Stop all services
	@echo "🛑 Stopping services..."
	@docker-compose down

logs: ## Show logs from all services
	@docker-compose logs -f

logs-api: ## Show logs from API service only
	@docker-compose logs -f api

clean: ## Stop services and remove volumes
	@echo "🧹 Cleaning up..."
	@docker-compose down -v
	@docker-compose down --rmi local

swagger: ## Generate OpenAPI/Swagger JSON file
	@python scripts/generate_openapi.py

migrate: ## Run database migrations
	@echo "🔄 Running database migrations..."
	@docker-compose exec api alembic upgrade head

migrate-auto: ## Generate automatic migration
	@read -p "Migration name: " name; \
	docker-compose exec api alembic revision --autogenerate -m "$$name"

init-db: ## Initialize database with sample data
	@echo "🏗️  Initializing database..."
	@docker-compose exec api python scripts/init_db.py

psql: ## Connect to PostgreSQL database
	@docker-compose exec postgres psql -U clinica_user -d clinica_360

test: ## Run tests (when implemented)
	@echo "🧪 Running tests..."
	@docker-compose exec api python -m pytest

dev: ## Start development environment
	@echo "🔧 Starting development environment..."
	@make setup
	@make up
	@echo "⏳ Waiting for services to be ready..."
	@sleep 5
	@make migrate
	@make init-db
	@echo ""
	@echo "🎉 Development environment ready!"
	@echo "🌐 Swagger UI: http://localhost:8000/docs"

build: ## Build application container
	@docker-compose build api



restart: ## Restart API service
	@docker-compose restart api

shell: ## Access API container shell
	@docker-compose exec api bash

status: ## Show services status
	@docker-compose ps 
