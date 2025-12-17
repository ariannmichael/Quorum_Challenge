# Backend - Django REST API

This is the backend service for the Quorum Challenge project, built with Django 4.2 and Django REST Framework.

> **Note**: This is part of a monorepo. For project-wide setup instructions, see the [main README](../README.MD).

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Database Setup](#database-setup)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Environment Variables](#environment-variables)
- [Docker](#docker)

## 🎯 Overview

The backend provides a RESTful API for managing bills, legislators, votes, and vote results. It follows Django's default structure and uses PostgreSQL as the database.

### Features

- **Bill Management**: Track bills with supporter and opposer counts
- **Legislator Management**: Track legislators with voting statistics
- **Vote Management**: Manage votes and vote results
- **CSV Import/Export**: Bulk import and export functionality
- **Analytics**: Get analytics for bills and legislators

## 🛠 Tech Stack

- **Framework**: Django 4.2.10
- **API**: Django REST Framework 3.14.0
- **Database**: PostgreSQL 17
- **Language**: Python 3.9+
- **Environment**: python-dotenv for configuration

## 📁 Project Structure

```
backend/
├── config/              # Django project settings
│   ├── settings.py     # Main settings file
│   ├── urls.py         # Root URL configuration
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── legislators/        # Legislators app
│   ├── models.py       # Legislator model
│   ├── views.py        # API views
│   ├── serializers.py  # DRF serializers
│   ├── urls.py         # App URLs
│   └── tests/          # Test files
├── bills/              # Bills app
│   ├── models.py       # Bill model
│   ├── views.py        # API views
│   ├── serializers.py  # DRF serializers
│   ├── urls.py         # App URLs
│   └── tests/          # Test files
├── votes/              # Votes app
│   ├── models.py       # Vote model
│   ├── views.py        # API views
│   ├── urls.py         # App URLs
│   └── tests/          # Test files
├── vote_results/       # Vote results app
│   ├── models.py       # VoteResult model
│   ├── views.py        # API views
│   ├── urls.py         # App URLs
│   └── tests/          # Test files
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image configuration
└── init-db.sh          # Database initialization script
```

## 📦 Installation

### Option 1: Using Makefile (Recommended)

From the project root:

```bash
make install-backend
```

### Option 2: Manual Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## 🏃 Running the Server

### Option 1: Using Makefile

From the project root:

```bash
make run-backend
```

### Option 2: Manual

```bash
# Activate virtual environment
source venv/bin/activate

# Run migrations (first time only)
python manage.py migrate

# Start development server
python manage.py runserver

# Server will be available at http://localhost:8000
```

### Option 3: Docker

From the project root:

```bash
make docker-up
# Or
docker-compose up backend
```

## 🗄️ Database Setup

### Using Docker (Recommended)

```bash
# Start PostgreSQL container
docker-compose up -d postgres

# Run migrations
make migrate
# Or manually:
python manage.py migrate
```

### Using Local PostgreSQL

1. Install PostgreSQL
2. Create database:
   ```sql
   CREATE DATABASE quorum_db;
   CREATE USER quorum_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE quorum_db TO quorum_user;
   ```
3. Update `settings.py` or `.env` file with database credentials
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

## 🔌 API Endpoints

Base URL: `http://localhost:8000/api/`

### Bills

- `GET /api/bills/analytics/` - Get bill analytics with supporter/opposer counts
- `POST /api/bills/import/` - Import bills from CSV file
- `GET /api/bills/export/` - Export bills analytics as CSV

**CSV Format for Import:**
```csv
id,title,sponsor_id
1,Example Bill,101
```

### Legislators

- `GET /api/legislators/analytics/` - Get legislator analytics with vote counts
- `POST /api/legislators/import/` - Import legislators from CSV file
- `GET /api/legislators/export/` - Export legislator analytics as CSV

**CSV Format for Import:**
```csv
id,name
1,John Doe
```

### Votes

- `POST /api/votes/import/` - Import votes from CSV file

**CSV Format for Import:**
```csv
id,bill_id
100,1
```

### Vote Results

- `POST /api/vote-results/import/` - Import vote results from CSV file

**CSV Format for Import:**
```csv
id,legislator_id,vote_id,vote_type
200,1,100,1
```

**Note**: `vote_type` is 1 for "yea" (support) and 2 for "nay" (oppose)

## 🧪 Testing

### Option 1: Using Makefile

From the project root:

```bash
make test-backend
```

### Option 2: Manual

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
python manage.py test

# Run specific app tests
python manage.py test legislators
python manage.py test bills
python manage.py test votes
python manage.py test vote_results
```

### Option 3: Docker

```bash
docker-compose exec backend python manage.py test
```

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Django Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=

# Database Configuration
POSTGRES_DB=quorum_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

**Note**: For Docker, environment variables are set in the root `.env` file or `docker-compose.yml`.

## 🐳 Docker

### Build Image

```bash
docker build -t quorum-backend .
```

### Run Container

```bash
docker run -p 8000:8000 \
  -e POSTGRES_HOST=postgres \
  -e POSTGRES_DB=quorum_db \
  -e POSTGRES_USER=quorum_user \
  -e POSTGRES_PASSWORD=quorum_password \
  quorum-backend
```

### Using Docker Compose

From the project root:

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Run migrations
docker-compose exec backend python manage.py migrate

# Run tests
docker-compose exec backend python manage.py test
```

## 📝 Django Management Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```

## 🏗️ Architecture

The backend follows Django's default structure:

- **Models**: Define database schema (`models.py`)
- **Views**: Handle HTTP requests (`views.py`)
- **Serializers**: Convert between Python objects and JSON (`serializers.py`)
- **URLs**: Route requests to views (`urls.py`)
- **Migrations**: Database schema changes (`migrations/`)

## 🔍 Development Tips

1. **Database Queries**: The project uses raw SQL for complex analytics queries for better performance
2. **Bulk Operations**: CSV imports use bulk_create for efficient database operations
3. **CORS**: CORS is enabled for all origins in development (configure properly for production)
4. **Environment**: Always use environment variables for sensitive data

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Main Project README](../README.MD)
- [Quick Start Guide](../QUICK_START.md)

## 🤝 Contributing

1. Follow Django coding conventions
2. Write tests for new features
3. Update migrations for model changes
4. Document API endpoints

## 📄 License

This project is part of the Quorum Challenge.

