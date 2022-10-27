"""Dictionary related utility functions."""

__author__ = "730576725"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table' (list of dictionaries)."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(all_data: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """We want to create a preview of a large dataset bc many rows are overwhelming, and someone might just want to see if they even opened the right file or are using the correct type of data."""
    preview: dict[str, list[str]] = {}
    for column in all_data:
        i: int = 0
        return_values: list[str] = []
        if n_rows >= len(all_data[column]):
            return all_data
        while i < n_rows:
            return_values.append(all_data[column][i]) 
            i += 1
        
        preview[column] = return_values
    return preview


def select(table_data: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Selects certain columns and creates a subset of data based on the selected rows."""
    subset: dict[str, list[str]] = {}
    for column in column_names:
        subset[column] = table_data[column]
    return subset


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function combines 2 tables without duplicate columns."""
    combined_table: dict[str, list[str]] = {}
    for column in table_1:
        combined_table[column] = table_1[column]
    for column in table_2:
        if column in combined_table:
            combined_table[column] += table_2[column]
        else:
            combined_table[column] = table_2[column]
    return combined_table


def count(value_list: list[str]) -> dict[str, int]:
    """This function tallies the amount of times unique values appear in a list."""
    counts: dict[str, int] = {}
    for value in value_list:
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1
    return counts