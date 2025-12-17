#!/bin/bash
set -e

echo "Initializing database..."

# The database is automatically created by PostgreSQL using POSTGRES_DB env var
# Django migrations will create all necessary tables
# This script is kept for any future custom initialization needs

echo "Database $POSTGRES_DB is ready for Django migrations."
