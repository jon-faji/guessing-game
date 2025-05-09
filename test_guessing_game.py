# guessing_game.py

# This is a test suite for a simple guessing game.
# The game generates a random secret number and the player has to guess it.
# The generate_secret function is mocked to return a fixed value for testing purposes.
# The test suite includes tests for correct guesses, too low/high guesses, and invalid input.
# This test suite uses unittest to test the evaluate_guess function and the generate_secret function.
# It includes tests for correct guesses, too low/high guesses, and invalid input.

import unittest
from guessing_game import evaluate_guess, generate_secret
from unittest.mock import patch

class TestGuessingGame(unittest.TestCase):

    def test_correct_guess(self):
        self.assertEqual(evaluate_guess(50, '50'), "Correct!")

    def test_too_low_guess(self):
        self.assertEqual(evaluate_guess(50, '30'), "Too low!")

    def test_too_high_guess(self):
        self.assertEqual(evaluate_guess(50, '70'), "Too high!")

    def test_invalid_input(self):
        self.assertEqual(evaluate_guess(50, 'hello'), "Invalid input. Please enter a number.")

    @patch('guessing_game.random.randint')
    def test_generate_secret_mocked(self, mock_randint):
        mock_randint.return_value = 42
        self.assertEqual(generate_secret(), 42)

if __name__ == "__main__":
    unittest.main()


