import unittest
from io import StringIO
import sys

def start_game():
    print("Welcome to the Text Adventure Game!")

class TestGame(unittest.TestCase):
    def test_start_game(self):
        captured_output = StringIO() # StringIO object captures the output.
        sys.stdout = captured_output # Redirects stdout to the StringIO object.

        start_game() # Calls the function to be tested.

        sys.stdout = sys.__stdout__  # Resets the redirection of the standard output sys.stdout back to its original value.

        output = captured_output.getvalue().strip() # Retrieves the value stored in the StringIO object (captured_output) as a string and stores it in output.

        self.assertEqual(output, "Welcome to the Text Adventure Game!")  # Checks if the output matches the expected value.

if __name__ == '__main__':
    unittest.main()
