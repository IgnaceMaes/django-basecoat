#!/bin/bash

# Quick start script for the Django Basecoat Demo Project

set -e

echo "🚀 Starting Django Basecoat Demo Setup"
echo ""

# Check if we're in the demo_project directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from the demo_project directory"
    exit 1
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed"
    echo "   Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Sync dependencies (uv will automatically install django-basecoat from parent dir)
echo "📦 Syncing dependencies with uv..."
uv sync

# Run migrations
echo "🗄️  Running database migrations..."
uv run python manage.py migrate --no-input

# Create superuser prompt
echo ""
read -p "Would you like to create a superuser? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    uv run python manage.py createsuperuser
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the development server, run:"
echo "  make run"
echo "  # or: uv run python manage.py runserver"
echo ""
echo "Then visit:"
echo "  - Home: http://127.0.0.1:8000/"
echo "  - Demo: http://127.0.0.1:8000/demo/"
echo "  - Admin: http://127.0.0.1:8000/admin/"
