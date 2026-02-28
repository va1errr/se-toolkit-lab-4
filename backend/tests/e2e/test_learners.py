"""Unit tests for learner validation edge cases."""

import pytest
from pydantic import ValidationError

from app.models.learner import LearnerCreate


def test_learner_create_with_empty_name_raises_validation_error() -> None:
    """Edge case: empty string for name should fail validation."""
    with pytest.raises(ValidationError):
        LearnerCreate(name="", email="test@example.com")


def test_learner_create_with_whitespace_only_name_raises_validation_error() -> None:
    """Edge case: whitespace-only name should fail validation."""
    with pytest.raises(ValidationError):
        LearnerCreate(name="   ", email="test@example.com")


def test_learner_create_with_valid_name_succeeds() -> None:
    """Normal case: valid name should pass validation."""
    learner = LearnerCreate(name="John Doe", email="john@example.com")
    assert learner.name == "John Doe"
    assert learner.email == "john@example.com"


def test_learner_create_with_very_long_name_succeeds() -> None:
    """Boundary value test: very long name (1000 chars) should pass validation."""
    long_name = "A" * 1000
    learner = LearnerCreate(name=long_name, email="test@example.com")
    assert learner.name == long_name
    assert len(learner.name) == 1000


def test_learner_create_with_single_char_name_succeeds() -> None:
    """Boundary value test: single character name should pass validation."""
    learner = LearnerCreate(name="A", email="test@example.com")
    assert learner.name == "A"


def test_learner_create_with_unicode_name_succeeds() -> None:
    """Edge case: unicode characters in name should pass validation."""
    learner = LearnerCreate(name="田中太郎", email="test@example.com")
    assert learner.name == "田中太郎"


def test_learner_create_with_empty_email_raises_validation_error() -> None:
    """Edge case: empty string for email should fail validation."""
    with pytest.raises(ValidationError):
        LearnerCreate(name="John Doe", email="")
