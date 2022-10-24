"""Testing functions for dictionary.py."""

__author__ = "730576725"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_large() -> None:
    """Dict is too large."""
    assert invert({}) == {}


def test_invert_samekey() -> None:
    """Tests to see if KeyError runs."""
    with pytest.raises(KeyError):
        first_last: dict[str, str] = {'Kris': 'Jordan', 'Maggie': 'Jordan'}
        invert(first_last)


def test_invert_usecase() -> None:
    """Usecase assert correct answer is returned."""
    assert invert({"maggie": "saunders", "kris": "jordan"}) == {'saunders': 'maggie', 'jordan': 'kris'}


def test_favorite_color_empty() -> None:
    """Edgecase if dict is empty."""
    names_colors: dict[str, str] = {}
    assert favorite_color(names_colors) == ""


def test_favorite_color_first() -> None:
    """If two colors appear same amt of times, return first."""
    assert favorite_color({"maggie": "blue", "kris": "blue", "zab": "green", "corey": "green"}) == "blue"


def test_favorite_color_correct() -> None:
    """If lesser color appears first, still return color with more instances."""
    assert favorite_color({"maggie": "blue", "zab": "green", "corey": "green"})


def test_count_empty() -> None:
    """If list of str's is empty, run code."""
    values: list[str] = ()
    assert count(values) == {}


def test_count_correct() -> None:
    """Return correct answer."""
    assert count(["joy", "maggie", "deb", "deb", "sofia"]) == {'joy': 1, 'maggie': 1, 'deb': 2, 'sofia': 1}


def test_count_only() -> None:
    """When only one type of item in list, return correct answer."""
    assert count(["hi", "hi", "hi"]) == {'hi': 3}