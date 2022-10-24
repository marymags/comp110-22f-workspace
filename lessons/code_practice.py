"""from 10/6/22 in-person class."""

# Instructions:
# Write a function named zip that has two lists of strings as parameters, and produces a dictionary where the keys
# are the items of the first list and the values are the corresponding items at the same index of the second list.
# you should assert that the length of the lists are equal, so that an error is produced if lists of unequal lengths are provided as arguemnts

def zip(list_a: list[str], list_b: list[int]) -> dict[str, int]:
    """"Build a dict from two lists."""
    assert len(list_a) == len(list_b)
    result: dict[str, int] = {}
    i: int = 0
    for key in list_a:
        result[key] = list_b[key[i]]
        i += 1
    return result

print(zip(list["hello", "world"], list[1, 2]))

# kris's version

def zip(ks: list[str], vs: list[str]) -> dict[str, str]:
    assert len(ks) == len(vs)
    result: dict[str, str] = {}
    for i in range(0, len(ks)):
        result [ks[i]] = vs[i]
    return result