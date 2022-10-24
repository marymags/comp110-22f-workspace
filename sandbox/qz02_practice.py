"""Practicing stuff from the qz02 practice guide."""

# Write a function called odd_and_even. Given a list of ints, odd_and_even 
# should return a new list containing the elements that 
# are odd and have an even index.
def odd_and_even(nums: list[int]) -> list[int]:
    i: int = 0
    newlist: list[int] = []
    while i < len(nums):
        if nums[i] % 2 != 0:
            newlist.append(nums[i])
        i += 2
    return newlist

print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))


# Write a function named vowels_and_threes. Given a string, 
# vowels_and_threes should return a new string containing the
#  characters that are either at an index that is a multiple of 3 
# or a vowel (one or the other, not both). You can assume that the
#  input string is all lowercase, for simplicity.
def vowels_and_threes(chars: str) -> str:
    """Takes str input and outputs characters contained in the original str if they are A: vowels or B: at an index multiple of 3."""
    vn3: str = ""
    i: int = 0
    vowel: list[str] = ["a", "e", "i", "o", "u"]
    for letter in chars:
        if letter in vowel:
            vn3 += letter
    while i < len(chars):
        if i % 3 == 0:
            vn3 += chars[i]
        i += 1
    return vn3


def average_grades(book: dict[str, list[int]]) -> dict[str, float]:
    """Ur_mom."""
    i: int = 0
    avgs: dict[str, float] = {}
    total: int = 0
    avg: float = 0.0
    for student in book:
        while i < len(book[student]):
            total += book[student][i]
            avg = total / len(book[student])
            avgs.append({student : avg})
            i += 1
    return avgs

print(average_grades({'Bill': [75, 94, 97], 'Annie': [88, 93, 99]}))

websters: dict[str, int] = {}
websters += {'Harry': 1}

print(websters)


