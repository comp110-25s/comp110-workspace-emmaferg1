"""Creating a wordle game!"""

__author__: str = "730566544"


def contains_char(searched_word: str, searched_char: str) -> bool:
    """Searching if single character is in word."""
    assert len(searched_char) == 1, f"len('{searched_char}') is not 1"
    idx: int = 0
    found_letter: bool = False
    while idx < len(searched_word):
        if searched_char == searched_word[idx]:
            found_letter = True
        idx += 1
        if found_letter is True:
            return True
        else:
            return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Color codifying the guess word."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess_word) == len(secret_word), "Guess must be same length as secret"
    idx: int = 0
    result: str = ""
    while idx < len(guess_word):
        if secret_word[idx] == guess_word[idx]:
            result += GREEN_BOX
        elif contains_char(searched_word=secret_word, searched_char=guess_word[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def input_guess(expected_length: int) -> str:
    """Checking if guess is the same length as secret word."""
    guess: str = input(f"Enter a {expected_length} character word:")
    if len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    else:
        return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    user_wins: bool = False
    while turn < 7:
        if user_wins is False:
            print(f"=== Turn {turn}/6 ===")
            final_guess: str = input_guess(len(secret))
            emojified(final_guess, secret)
            if final_guess == secret:
                print(f"You won in {turn}/6 turns!")
                user_wins = True
        turn += 1
    if user_wins is not True:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
