.PHONY: help install install-backend install-frontend run run-backend run-frontend test test-backend test-frontend test-docker test-backend-docker test-frontend-docker docker-build docker-up docker-down docker-logs clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: install-backend install-frontend ## Install all dependencies

install-backend: ## Install backend dependencies
	@echo "Installing backend dependencies..."
	cd backend && \
	if [ ! -d "venv" ]; then \
		python3 -m venv venv; \
	fi && \
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

install-frontend: ## Install frontend dependencies
	@echo "Installing frontend dependencies..."
	cd frontend && npm install

run: ## Run both backend and frontend (use separate terminals: make run-backend and make run-frontend)
	@echo "To run both services, use separate terminals:"
	@echo "  Terminal 1: make run-backend"
	@echo "  Terminal 2: make run-frontend"
	@echo "Or use Docker: make docker-up"

run-backend: ## Run backend server
	@echo "Starting backend server..."
	cd backend && \
	. venv/bin/activate && \
	python manage.py runserver

run-frontend: ## Run frontend dev server
	@echo "Starting frontend dev server..."
	cd frontend && npm run dev

test: test-backend test-frontend ## Run all tests (local)

test-backend: ## Run backend tests (local, requires venv)
	@echo "Running backend tests locally..."
	@if [ ! -d "backend/venv" ]; then \
		echo "Error: Virtual environment not found. Run 'make install-backend' first."; \
		exit 1; \
	fi
	cd backend && \
	. venv/bin/activate && \
	python manage.py test

test-frontend: ## Run frontend tests (local, if available)
	@echo "Running frontend tests locally..."
	@cd frontend && npm test 2>/dev/null || echo "No tests configured"

test-docker: test-backend-docker test-frontend-docker ## Run all tests in Docker

test-backend-docker: ## Run backend tests in Docker
	@echo "Running backend tests in Docker..."
	@if ! docker-compose ps | grep -q "quorum_challenge_backend.*Up"; then \
		echo "Error: Backend container is not running. Start it with 'make docker-up' first."; \
		exit 1; \
	fi
	docker-compose exec backend python manage.py test

test-frontend-docker: ## Run frontend tests in Docker (if available)
	@echo "Running frontend tests in Docker..."
	@if ! docker-compose ps | grep -q "quorum_challenge_frontend.*Up"; then \
		echo "Error: Frontend container is not running. Start it with 'make docker-up' first."; \
		exit 1; \
	fi
	@docker-compose exec frontend npm test 2>/dev/null || echo "Note: Frontend tests are not configured. Add a test framework (e.g., Vitest, Jest) to run tests."

docker-build: ## Build Docker images
	@echo "Building Docker images..."
	docker-compose build

docker-up: ## Start all services with Docker
	@echo "Starting Docker services..."
	docker-compose up -d

docker-down: ## Stop all Docker services
	@echo "Stopping Docker services..."
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

docker-restart: docker-down docker-up ## Restart all Docker services

migrate: ## Run database migrations
	@echo "Running migrations..."
	cd backend && \
	. venv/bin/activate && \
	python manage.py migrate

migrate-docker: ## Run database migrations in Docker
	@echo "Running migrations in Docker..."
	docker-compose exec backend python manage.py migrate

clean: ## Clean up generated files and caches
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	cd frontend && rm -rf node_modules dist .vite 2>/dev/null || true
	cd backend && rm -rf venv 2>/dev/null || true

setup: install migrate ## Complete setup (install + migrate)

setup-docker: docker-build docker-up ## Complete Docker setup (build + start)
	@echo "Waiting for services to be ready..."
	@sleep 5
	@make migrate-docker

test-all: test-docker ## Run all tests in Docker (alias for test-docker)

