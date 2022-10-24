"""EX07 working with dictionaries. This file is where we implement function skeletons."""

__author__ = "730576725"


def invert(first_last: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings, this function returns that dictionary with the keys and values inverted."""
    last_first: dict[str, str] = {}
    for first in first_last:
        if first_last[first] in last_first:
            raise KeyError("There seem to be duplicate names.")
        last_first[first_last[first]] = first
    return last_first


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns most frequent color in a list of names and favorite colors."""
    mode_color: dict[str, int] = {}
    favorite: str = ""
    most: int = 0
    for names in names_colors:
        if names_colors[names] not in mode_color:
            mode_color[names_colors[names]] = 1
        else:
            mode_color[names_colors[names]] += 1
    for colors in mode_color:
        if mode_color[colors] > most:
            favorite = colors
            most = mode_color[colors]
    return favorite


def count(values: list[str]) -> dict[str, int]:
    """This is a docstring. Love you Kris but my brain is broken."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 0
            result[value] += 1 
    return result