# Quick Start Guide

## 🚀 Fastest Way to Get Started

### Option 1: Docker (Recommended - Easiest)

```bash
# One command to rule them all
make setup-docker

# That's it! Services are running:
# - Backend: http://localhost:8000
# - Frontend: http://localhost:5173
# - Database: localhost:5432
```

### Option 2: Local Development

```bash
# 1. Install everything
make install

# 2. Start database (if not using Docker)
docker-compose up -d postgres

# 3. Run migrations
make migrate

# 4. Start backend (Terminal 1)
make run-backend

# 5. Start frontend (Terminal 2)
make run-frontend
```

## 📋 Common Commands

```bash
# See all available commands
make help

# Install dependencies
make install

# Run tests (Docker - recommended when using Docker)
make test-docker

# Or run tests locally (requires venv setup)
make test

# Docker operations
make docker-up      # Start all services
make docker-down    # Stop all services
make docker-logs    # View logs
make docker-build   # Rebuild images

# Database
make migrate        # Run migrations locally
make migrate-docker  # Run migrations in Docker
```

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Stop existing services
make docker-down
# Or kill process on port
lsof -ti:8000 | xargs kill  # Backend
lsof -ti:5173 | xargs kill  # Frontend
```

### Database Connection Issues
```bash
# Check if database is running
docker-compose ps

# Restart database
docker-compose restart postgres
```

### Clean Start
```bash
# Clean everything and start fresh
make clean
make docker-down
docker-compose down -v  # Remove volumes
make setup-docker
```

## 📝 Environment Variables

Create a `.env` file in the root directory:

```env
POSTGRES_DB=quorum_db
POSTGRES_USER=quorum_user
POSTGRES_PASSWORD=quorum_password
DEBUG=True
SECRET_KEY=your-secret-key
```

## 🎯 Next Steps

1. Visit http://localhost:5173 for the frontend
2. Visit http://localhost:8000/api/ for the API
3. Check the main README.MD for detailed documentation

