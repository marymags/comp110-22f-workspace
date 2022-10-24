"""ex03 - Structured Wordle."""

__author__ = "730576725"


def contains_char(any_length: str, single_char: str) -> bool:
    """Function's purpose is to check if a single character is contained within the given word."""
    assert len(single_char) == 1
    any_length_index: int = 0
    while any_length_index < len(any_length):
        if any_length[any_length_index] == single_char:
            return True
        else:
            any_length_index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Function's purpose is to return wordle colored boxes when given two strings of equal length."""
    assert len(guess) == len(secret)
    emoji_string: str = ""
    index: int = 0
    """Declaring emoji variables."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX
            index += 1
        else:
            if contains_char(secret, guess[index]) is True:
                emoji_string += YELLOW_BOX
                index += 1
            else:
                emoji_string += WHITE_BOX
                index += 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """The purpose of this function is to establish an expected length of the word, then prompt the user for a word of that length."""
    entered_word = input(f"Enter a {expected_length} character word: ")
    while len(entered_word) != expected_length:
        entered_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return entered_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    correct_word: str = "codes"
    to_win: bool = False

    while turns <= 6 and to_win is False:
        print(f"=== Turn {turns}/6 ===")
        entered_word = input_guess(len(correct_word))
        print(emojified(entered_word, correct_word))

        if entered_word == correct_word:
            to_win = True
            print(f"You won in {turns}/6 turns!")
        else:
            turns += 1

    if to_win is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()