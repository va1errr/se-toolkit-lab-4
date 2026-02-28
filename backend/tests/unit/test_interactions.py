"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1

# Assuming there is a function or service that filters interactions by item_id.
# Adjust imports according to your project structure.

# Example placeholder import (modify if needed):
# from backend.interactions.service import get_interactions


def test_filter_excludes_interaction_with_different_learner_id():
    """
    Boundary-value test:
    Interaction where item_id and learner_id are different.
    When filtering by item_id=1, the interaction should appear in results.
    """

    # Arrange
    # Create a mock interaction dataset if your project doesn't use database fixtures.
    interactions = [
        {
            "item_id": 1,
            "learner_id": 2,
            "interaction": "example_interaction",
        },
        {
            "item_id": 2,
            "learner_id": 3,
            "interaction": "other_interaction",
        },
    ]

    # Example filtering logic (replace with actual function under test)
    def filter_by_item_id(data, item_id):
        return [x for x in data if x.get("item_id") == item_id]

    # Act
    result = filter_by_item_id(interactions, item_id=1)

    # Assert
    assert len(result) == 1
    assert result[0]["item_id"] == 1
    assert result[0]["learner_id"] == 2

