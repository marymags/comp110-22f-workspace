"""Some tender, loving functions"""


from email.policy import strict


def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string"""
    return f"I love you {subject}!"

print(love("Maggie"))

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

print(spread_love("Maggie", 6))

