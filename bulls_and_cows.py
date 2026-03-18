"""hm8_job1"""
import random


def bulls_and_cows():
    """
    This is a variant of the game "Bulls and Cows", where a person plays against a computer.
    The computer generates a secret 4-digit number with non-repeating digits.
    The player is trying to guess the number. An attempt is to enter a 4-digit number with non-repeating digits.
    In response, the computer tells you
    how many digits are guessed without matching their positions in the secret number (i.e., the number of cows)
    and how many are guessed up to the position in the secret number (i.e., the number of bulls).
    The player enters the combinations one by one until he guesses the whole sequence.
    """
    secret = random.sample("0123456789", 4)
    while True:
        number = input("Guess the number: ")
        if len(number) != 4 or not number.isdigit() or len(set(number)) != 4:
            print("You need to enter 4-digit number with non-repeating digits")
            continue
        bulls = sum(1 for i in range(4) if number[i] == secret[i])
        cows = sum(1 for i in range(4) if number[i] in secret and number[i] != secret[i])
        print(f"Result: {bulls} bulls, {cows} cows")
        if bulls == 4:
            print('WIN!!!')
            break


bulls_and_cows()
