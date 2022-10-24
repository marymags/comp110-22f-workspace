"""EX05 testing utils.py."""

__author__ = "730576725"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Edgecase makes sure code doesn't run when list is empty."""
    any_list: list[int] = []
    assert only_evens(any_list) == []


def test_only_evens_answer() -> None:
    """Usecase assert answer is 2 when given list is 1, 2, 3."""
    assert only_evens(1, 2, 3) == [2]


def test_only_evens_multi_evens() -> None:
    """Usecase assert when multiple evens in list, multiple evens are returned."""
    assert only_evens([1, 2, 2, 2, 3, 4, 4]) == [2, 2, 2, 4, 4]


def test_concat_empty() -> None:
    """Edgecase make sure code doesn't run when list is empty."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_answer() -> None:
    """Usecase assert answer is 1 2 3 4 when lists are 1, 2 and 3, 4."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_concat_single() -> None:
    """Usecase assert answer is 1 2 and list works when list length is 1."""
    assert concat([1], [2]) == [1, 2]


def test_sub_empty() -> None:
    """Edgecase don't run code when list is empty."""
    listy: list[int] = []
    assert sub(listy, 8, -1) == []


def test_sub_answer() -> None:
    """Usecase assert correct answer (when list is 1, 2, 3, 4, 5 and start is 1 and end is 4, answer is 2, 3, 4)."""
    listy: list[int] = [1, 2, 3, 4, 5]
    assert sub(listy, 1, 4) == [2, 3, 4]


def test_sub_negative() -> None:
    """If start index is less than 0, use 0 as start index."""
    listy: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(listy, -1, 2) == [1, 2, 3]