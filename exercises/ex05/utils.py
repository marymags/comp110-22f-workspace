"""EX05 working with unit tests."""

__author__ = "730576725"


def only_evens(any_list: list[int]) -> list[int]:
    """Given a list of ints, only_evens will return a list of all the even items in the given list."""
    i: int = 0
    even_list: list = list()
    while i < len(any_list):
        if any_list[i] % 2 == 0:
            even_list.append(any_list[i])
        i += 1
    return even_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """When given two lists of ints, concat will return a list containing both initial lists."""
    first_i: int = 0
    second_i: int = 0
    combined_list: list = list()
    while first_i < len(first_list): 
        combined_list.append(first_list[first_i])
        first_i += 1
    while second_i < len(second_list):
        combined_list.append(second_list[second_i])
        second_i += 1
    return combined_list


def sub(listy: list[int], start: int, end: int) -> list[int]:
    """When given a list and two indexes, return items in the list between those two indexes."""
    returned_list: list[int] = list()
    if end <= 0:
        return []
    if end > len(listy):
        end = len(listy)
    if start < 0:
        start = 0
    if start > len(listy):
        return []
    while start < end:
        returned_list.append(listy[start])
        start += 1
    return returned_list
