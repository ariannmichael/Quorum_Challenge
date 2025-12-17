# Quorum Challenge - Monorepo

A full-stack application for displaying bills and legislators with vote analytics, built with Django REST Framework and React.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Docker Setup](#docker-setup)
- [Available Commands](#available-commands)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

## 🎯 Overview

This project displays bills with their supporter and opposer counts, and legislators with the bills they supported and opposed. The project follows Django's default structure and is organized as a monorepo with both backend and frontend.

The application allows users to:
- View bill analytics with supporter and opposer counts
- View legislator analytics showing bills they supported and opposed
- Import data via CSV files (bills, legislators, votes, vote results)
- Export analytics data as CSV files
- Access a modern React-based frontend interface

## ✨ Features

- **Bill Analytics**: View all bills with supporter and opposer counts
- **Legislator Analytics**: View all legislators with their voting statistics
- **CSV Import**: Bulk import data for bills, legislators, votes, and vote results
- **CSV Export**: Download analytics data as CSV files
- **RESTful API**: Django REST Framework backend with comprehensive endpoints
- **Modern Frontend**: React 19 with TypeScript and Vite
- **Docker Support**: Full containerization for easy deployment
- **Monorepo Structure**: Unified commands for both backend and frontend

## 🛠 Tech Stack

- **Backend**: 
  - Django 4.2
  - Django REST Framework 3.14
  - Python 3.9+
  - PostgreSQL 17
- **Frontend**: 
  - React 19
  - TypeScript 5.7
  - Vite 6.2
  - React Router 7
  - Bootstrap 5
- **DevOps**: 
  - Docker & Docker Compose
  - Makefile for unified commands

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** (for local development)
- **Node.js 18+** and npm (for local development)
- **Docker** and **Docker Compose** (for containerized development)
- **PostgreSQL** (optional, if not using Docker)
- **Make** (optional, but recommended for easy command execution)

> **Note**: If you're using Docker, you only need Docker and Docker Compose installed.

## 📁 Project Structure

```
.
├── backend/              # Django backend application
│   ├── config/          # Django settings
│   ├── legislators/     # Legislators app
│   ├── bills/           # Bills app
│   ├── votes/           # Votes app
│   ├── vote_results/    # Vote results app
│   ├── Dockerfile       # Backend Docker image
│   └── requirements.txt # Python dependencies
├── frontend/            # React frontend application
│   ├── src/            # Source files
│   ├── Dockerfile      # Frontend Docker image
│   └── package.json    # Node dependencies
├── docker-compose.yml   # Docker services orchestration
├── Makefile            # Common commands
├── package.json        # Root npm scripts
├── .gitignore         # Git ignore rules
├── .dockerignore       # Docker ignore rules
├── README.MD           # This file
├── QUICK_START.md      # Quick reference guide
└── Q&A.MD             # Q&A document
```

## 🚀 Quick Start

> 💡 **New to the project?** Check out [QUICK_START.md](./QUICK_START.md) for a faster getting started guide!

### Using Docker (Recommended - Easiest)

```bash
# One command to get everything running
make setup-docker

# That's it! Services are now available:
# - Backend API: http://localhost:8000
# - Frontend: http://localhost:5173
# - Database: localhost:5432
```

### Using Local Development

```bash
# 1. Install all dependencies
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

## 📦 Installation

### Option 1: Using Makefile (Recommended)

```bash
# Install all dependencies
make install

# Or install separately:
make install-backend
make install-frontend
```

### Option 2: Manual Installation

#### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Frontend

```bash
cd frontend
        npm install
        ```

## 🏃 Running the Project

### Option 1: Using Makefile

```bash
# Run backend and frontend in separate terminals
make run-backend    # Terminal 1 - Backend on http://localhost:8000
make run-frontend   # Terminal 2 - Frontend on http://localhost:5173

# Or see instructions:
make run
```

### Option 2: Manual

#### Backend

```bash
cd backend
source venv/bin/activate
        python manage.py runserver
# Server runs on http://localhost:8000
```

#### Frontend

```bash
cd frontend
npm run dev
# Server runs on http://localhost:5173
```

### Option 3: Docker

```bash
# Start all services
make docker-up

# Or manually:
docker-compose up -d

# View logs
make docker-logs
# Or: docker-compose logs -f
```

## 🧪 Testing

### Option 1: Using Makefile

```bash
# Run all tests
make test

# Or run separately:
make test-backend
make test-frontend
```

### Option 2: Manual

#### Backend

```bash
cd backend
source venv/bin/activate
python manage.py test
```

#### Frontend

```bash
cd frontend
npm test
```

### Option 3: Docker

```bash
# Run backend tests in Docker
docker-compose exec backend python manage.py test
```

## 🐳 Docker Setup

### Prerequisites

- Docker and Docker Compose installed

### Environment Variables

Create a `.env` file in the root directory. You can reference the structure below:

```env
# Database Configuration
POSTGRES_DB=quorum_db
POSTGRES_USER=quorum_user
POSTGRES_PASSWORD=quorum_password
POSTGRES_PORT=5432

# Backend Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
BACKEND_PORT=8000

# Frontend Configuration
FRONTEND_PORT=5173
VITE_API_URL=http://localhost:8000
```

> **Note**: For Docker, environment variables can be set in the `.env` file or directly in `docker-compose.yml`. For local development, create a `.env` file in the `backend/` directory (see `backend/.env.example`).

### Docker Commands

```bash
# Build images
make docker-build

# Start services
make docker-up

# Stop services
make docker-down

# View logs
make docker-logs

# Restart services
make docker-restart

# Run migrations in Docker
make migrate-docker
```

### Services

- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:5173
- **PostgreSQL**: localhost:5432

## 📝 Available Commands

### Makefile Commands

| Command | Description |
|---------|-------------|
| `make help` | Show all available commands |
| `make install` | Install all dependencies |
| `make install-backend` | Install backend dependencies |
| `make install-frontend` | Install frontend dependencies |
| `make run` | Show instructions for running services |
| `make run-backend` | Run backend server |
| `make run-frontend` | Run frontend dev server |
| `make test` | Run all tests |
| `make test-backend` | Run backend tests |
| `make test-frontend` | Run frontend tests |
| `make migrate` | Run database migrations |
| `make migrate-docker` | Run migrations in Docker |
| `make docker-build` | Build Docker images |
| `make docker-up` | Start Docker services |
| `make docker-down` | Stop Docker services |
| `make docker-logs` | View Docker logs |
| `make docker-restart` | Restart Docker services |
| `make setup` | Complete setup (install + migrate) |
| `make setup-docker` | Complete Docker setup |
| `make clean` | Clean up generated files |

## 🔌 API Endpoints

### Base URL
- Local: `http://localhost:8000/api/`
- Docker: `http://localhost:8000/api/`

### Endpoints

#### Bills
- `GET /api/bills/analytics/` - Get bill analytics
- `POST /api/bills/import/` - Import bills from CSV
- `GET /api/bills/export/` - Export bills as CSV

#### Legislators
- `GET /api/legislators/analytics/` - Get legislator analytics
- `POST /api/legislators/import/` - Import legislators from CSV
- `GET /api/legislators/export/` - Export legislators as CSV

#### Votes
- `POST /api/votes/import/` - Import votes from CSV

#### Vote Results
- `POST /api/vote-results/import/` - Import vote results from CSV

## 🧹 Cleanup

```bash
# Clean up generated files and caches
make clean

# Stop and remove Docker containers
make docker-down

# Remove Docker containers and volumes (complete cleanup)
docker-compose down -v
```

## 🔧 Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8000 (backend)
lsof -ti:8000 | xargs kill

# Kill process on port 5173 (frontend)
lsof -ti:5173 | xargs kill

# Or use Docker instead
make docker-up
```

### Database Connection Issues

```bash
# Check if database is running
docker-compose ps

# Restart database service
docker-compose restart postgres

# View database logs
docker-compose logs postgres
```

### Migration Issues

```bash
# Reset migrations (⚠️ This will delete data)
make docker-down
docker-compose down -v
make setup-docker

# Or manually reset
cd backend
source venv/bin/activate
python manage.py migrate --run-syncdb
```

### Frontend Can't Connect to Backend

1. Ensure backend is running: `make run-backend` or `docker-compose up backend`
2. Check `VITE_API_URL` in your `.env` file matches your backend URL
3. For Docker, ensure both services are on the same network

### Python Virtual Environment Issues

```bash
# Recreate virtual environment
cd backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📚 Additional Notes

- **Architecture**: The backend uses Django's default structure (not DDD/Clean Architecture)
- **Database**: Migrations are handled automatically in Docker
- **Environment Variables**: Can be set via `.env` file or Docker Compose
- **API Connection**: The frontend automatically connects to the backend API
- **Performance**: Uses bulk inserts and optimized queries for better performance
- **CSV Format**: Ensure CSV files follow the expected format for imports

## 📖 Additional Resources

- **[QUICK_START.md](./QUICK_START.md)**: Quick reference guide for common tasks
- **[Q&A.MD](./Q&A.MD)**: Answers to common questions about the solution

## 🤝 Contributing

1. Install dependencies: `make install`
2. Run migrations: `make migrate`
3. Start development servers: 
   - Terminal 1: `make run-backend`
   - Terminal 2: `make run-frontend`
4. Run tests: `make test`
5. Make your changes and test thoroughly

## 📄 License

This project is part of the Quorum Challenge.
