# Django Basecoat Demo Project

This is a demo Django application that showcases the django-basecoat component library in action.

## Overview

This demo project demonstrates how to use django-basecoat in a real Django application. It includes:

- A landing page with information about django-basecoat
- A comprehensive kitchen sink demo page showing all available components
- Proper Django project structure using django-basecoat as a library

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Fast Python package installer and resolver

## Setup

### Quick Start (Recommended)

Just run the quickstart script:

```bash
cd demo_project
./quickstart.sh
```

That's it! The script will:
- Install all dependencies (including django-basecoat from the parent directory)
- Run database migrations
- Offer to create a superuser

### Manual Setup

1. **Install uv (if not already installed):**

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Sync dependencies:**

   ```bash
   uv sync
   ```

   This automatically installs django-basecoat from the parent directory.

3. **Run migrations:**

   ```bash
   uv run python manage.py migrate
   ```

4. **Run the development server:**

   ```bash
   uv run python manage.py runserver
   ```

### Using Make

```bash
make setup  # Sync dependencies and run migrations
make run    # Start the development server
```

### Visit the Demo

Open your browser and navigate to:
- Home: http://127.0.0.1:8000/
- Component Demo: http://127.0.0.1:8000/demo/

## Project Structure

```
demo_project/
├── manage.py                 # Django management script
├── settings.py              # Django settings
├── urls.py                  # Project URL configuration
├── wsgi.py                  # WSGI configuration
├── asgi.py                  # ASGI configuration
└── demo_app/                # Demo application
    ├── __init__.py
    ├── apps.py
    ├── views.py             # View functions
    ├── urls.py              # App URL patterns
    ├── models.py
    ├── admin.py
    └── templates/
        └── demo_app/
            ├── index.html   # Landing page
            └── demo.html    # Kitchen sink demo
```

## Usage in Your Own Projects

To use django-basecoat in your own Django projects:

1. **Install django-basecoat:**

   With uv:
   ```bash
   uv add django-basecoat django-cotton
   ```

   Or with pip:
   ```bash
   pip install django-basecoat django-cotton
   ```

2. **Add to INSTALLED_APPS:**

   ```python
   INSTALLED_APPS = [
       # ...
       "django_cotton",
       "django_basecoat",
       # ...
   ]
   ```

3. **Configure templates:**

   ```python
   TEMPLATES = [
       {
           "BACKEND": "django.template.backends.django.DjangoTemplates",
           "DIRS": [],
           "APP_DIRS": True,
           "OPTIONS": {
               "builtins": [
                   "django_cotton.templatetags.cotton",
               ],
           },
       },
   ]
   ```

4. **Use components in your templates:**

   ```django
   <c-button variant="default">Click me</c-button>
   <c-card>
       <c-card.header>
           <h2>Card Title</h2>
       </c-card.header>
       <c-card.section>
           Card content goes here.
       </c-card.section>
   </c-card>
   ```

## Available Components

The demo showcases all available components including:

- Accordion
- Alert
- Avatar
- Badge
- Breadcrumb
- Button & Button Group
- Card (with header, section, footer)
- Checkbox
- Command Menu
- Dialog
- Dropdown Menu
- Empty State
- Field (with error and hint)
- Form
- Input & Input Group
- Item
- Kbd
- Label
- Pagination
- Popover
- Progress
- Radio & Radio Group
- Select
- Separator
- Sidebar
- Skeleton
- Slider
- Spinner
- Switch
- Tabs
- Table
- Textarea
- Toaster
- Tooltip

## Notes

- This demo project is **not** included in the published django-basecoat package
- It's meant for development and demonstration purposes only
- The demo uses Basecoat CSS from CDN for simplicity
- In production, you may want to install and bundle Basecoat CSS locally

## Learn More

- [django-basecoat GitHub](https://github.com/IgnaceMaes/django-basecoat)
- [Basecoat CSS](https://basecoat.dev/)
- [django-cotton](https://django-cotton.com/)
- [Django Documentation](https://docs.djangoproject.com/)
