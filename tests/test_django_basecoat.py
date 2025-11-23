"""Tests for django_basecoat."""

import django_basecoat


def test_version() -> None:
    """Test version is defined."""
    assert hasattr(django_basecoat, "__version__")
    assert isinstance(django_basecoat.__version__, str)
