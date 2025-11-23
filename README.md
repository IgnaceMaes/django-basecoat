[![CI/CD](https://github.com/IgnaceMaes/django-basecoat/actions/workflows/checks.yml/badge.svg)](https://github.com/IgnaceMaes/django-basecoat/actions/workflows/release-please.yml)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/IgnaceMaes/django-basecoat)](https://github.com/IgnaceMaes/django-basecoat/releases)
[![PyPI version](https://badge.fury.io/py/django-basecoat.svg)](https://badge.fury.io/py/django-basecoat)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-basecoat.svg)](https://pypi.org/project/django-basecoat/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked with mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](http://mypy-lang.org/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
# django-basecoat

Ready-made [Basecoat](https://basecoatui.com/) components ([shadcn/ui](https://ui.shadcn.com/)) for Django, powered by [django-cotton](https://django-cotton.com/).

## Installation

```bash
uv add django-cotton django-basecoat
```

Add `django_basecoat` and `django_cotton` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "django_cotton",
    "django_basecoat",
    ...
]
```

## Quick Start

Include the required CSS and JS in your base template (or use your own setup):

```html
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/basecoat-css@0.3.6/dist/basecoat.cdn.min.css">
<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3.6/dist/js/all.min.js" defer></script>
```

Use components in your templates:

```django
<c-button>Click me</c-button>
<c-card>
    <c-card.header>Card Title</c-card.header>
    <c-card.section>Card content goes here</c-card.section>
</c-card>
```

Available components include: accordion, alert, avatar, badge, breadcrumb, button, card, checkbox, dialog, dropdown menu, input, select, table, tabs, and more.

## Documentation

- **[Setup Guide](https://github.com/IgnaceMaes/django-basecoat/blob/main/SETUP.md)** - Initial project configuration
- **[Development Workflow](https://github.com/IgnaceMaes/django-basecoat/blob/main/WORKFLOW.md)** - How to contribute and work with the project

## Demo Project

Want to see django-basecoat in action? Check out the **[demo_project](demo_project/)** directory for a complete Django application showcasing all available components.

To run the demo:

```bash
cd demo_project
./quickstart.sh
# or: make setup && make run
```

Then visit http://127.0.0.1:8000/ to see the component library in action!
