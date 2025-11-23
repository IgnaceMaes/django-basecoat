.PHONY: help sync migrate run clean superuser setup

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

sync: ## Sync dependencies with uv
	uv sync

migrate: ## Run database migrations
	uv run python manage.py migrate

run: ## Start the development server
	uv run python manage.py runserver

clean: ## Remove database and cache files
	rm -f db.sqlite3
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

superuser: ## Create a superuser
	uv run python manage.py createsuperuser

setup: sync migrate ## Complete setup (sync + migrate)
	@echo "✅ Setup complete! Run 'make run' to start the server."
