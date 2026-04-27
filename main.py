import random

def get_random_number(lower, upper):
    return random.randint(lower, upper)

def get_user_guess(lower, upper):
    while True:
        try:
            guess = int(input(f"Enter your guess ({lower}-{upper}): "))
            if lower <= guess <= upper:
                return guess
            else:
                print(f"Please enter a number between {lower} and {upper}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def play_game():
    lower = 1
    upper = 100
    number_to_guess = get_random_number(lower, upper)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower} and {upper}.")
    while True:
        user_guess = get_user_guess(lower, upper)
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()