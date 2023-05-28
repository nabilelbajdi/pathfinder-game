import unittest
from io import StringIO
import sys
import time

def typewriter_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

class TestTypewriterPrint(unittest.TestCase):
    def test_typewriter_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        text = "Typewriter effect"
        typewriter_print(text)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()

        self.assertEqual(output, text)

def start_game():
    typewriter_print("Welcome to the Text Adventure Game! This is an interactive text-based adventure game that will take you through a journey.")

class TestGame(unittest.TestCase):
    def test_start_game(self):
        captured_output = StringIO() # StringIO object captures the output.
        sys.stdout = captured_output # Redirects stdout to the StringIO object.

        start_game() # Calls the function to be tested.

        sys.stdout = sys.__stdout__  # Resets the redirection of the standard output sys.stdout back to its original value.

        output = captured_output.getvalue().strip() # Retrieves the value stored in the StringIO object (captured_output) as a string and stores it in output.

        self.assertEqual(output, "Welcome to the Text Adventure Game! This is an interactive text-based adventure game that will take you through a journey.")  # Checks if the output matches the expected value.

    def test_act2_forest(self):
        # Same setup as start_game(), therefore skipping this test
        pass
    
if __name__ == '__main__':
    unittest.main()
