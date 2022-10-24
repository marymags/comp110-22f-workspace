"""EX04 utils."""

__author__ = "730576725"


def all(numbers: list[int], single_num: int) -> bool:
    """Checks to see if all items int in a list match one given int."""
    numbers_index: int = 0
    if len(numbers) == 0:
        return False
    while numbers_index < len(numbers):
        if numbers[numbers_index] == single_num:
            numbers_index += 1
        else:
            return False
    return True


def max(number_list: list[int]) -> int:
    """A function that returns the largest integer in a list of integers."""
    nl_index: int = 1
    largest_int: int = 0
    if len(number_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        if number_list[0] > number_list[nl_index]:
            largest_int = number_list[0]
        else:
            largest_int = number_list[nl_index]
        nl_index += 1
    while nl_index < len(number_list):
        if number_list[nl_index] > largest_int:
            largest_int = number_list[nl_index]
        else:
            largest_int = largest_int
        nl_index += 1
    return largest_int


def is_equal(a_list: list[int], b_list: list[int]) -> bool:
    """Checks if two lists are deeply equal to each other."""
    a_index: int = 0
    b_index: int = 0
    if len(a_list) != len(b_list):
        return False
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] == b_list[b_index]:
            a_index += 1
            b_index += 1
        else:
            return False
    return True