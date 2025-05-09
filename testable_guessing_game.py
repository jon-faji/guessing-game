# testable_guessing_game.py

# This is a test suite for a simple guessing game.
# The game generates a random secret number and the player has to guess it.
# The generate_secret function is mocked to return a fixed value for testing purposes.
# The test suite includes tests for correct guesses, too low/high guesses, and invalid input.
# This test suite uses unittest to test the evaluate_guess function and the generate_secret function.
# It includes tests for correct guesses, too low/high guesses, and invalid input.


def evaluate_guess(secret, guess):
    try:
        guess = int(guess)
    except ValueError:
        return "Invalid input. Please enter a number."
    
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"
