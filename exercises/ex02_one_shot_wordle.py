"""EX02 - One-Shot Wordle - Loops."""

__author__ = "730576725"

"""declaring variables"""

secret_word: str = "hi"
character_number: int = len(secret_word)
guess_word: str = input(f"What is your {character_number}-letter guess? ")
guess_index: int = 0
secret_index: int = 0
emoji_string: str = ""

"""declaring emoji variables"""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""if the length of guess doesn't match secret word."""

while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {character_number} letters! Try again: ")

"""if length of guess matches secret word, but is not secret word."""

if len(guess_word) == len(secret_word) and guess_word != secret_word:
    while secret_index < len(secret_word):
        guess_index = 0
        on_off: bool = False
        if guess_word[secret_index] == secret_word[secret_index]:
            emoji_string += GREEN_BOX
        if guess_word[secret_index] != secret_word[secret_index]:
            while on_off is not True and guess_index < len(guess_word):
                if guess_word[secret_index] == secret_word[guess_index]:
                    on_off = True
                guess_index += 1
            if on_off is not True:
                emoji_string += WHITE_BOX
            else:
                emoji_string += YELLOW_BOX
        secret_index += 1
    print(emoji_string)
    print("Not quite. Play again soon!")

"""if guess matches secret word."""

if guess_word == secret_word:
    print("Woo! You got it!")
    print("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")