import os
import sys
import time

# Function to give a typewriter effect for print statements
def typewriter_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Typing speed
    print()  # This will move to the next line after printing the whole text

# Prints welcome message and descsription of the game when starting it
def start_game():
    typewriter_print("Welcome to the Text Adventure Game! This is an interactive text-based adventure game that will take you through a journey.")
    input("Press Enter to start the game ")

def clear_screen():
    # Clear the terminal screen after the welcome message above
    if os.name == 'posix':  # For UNIX/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        # For unsupported operating systems, it will do nothing.
        pass

# Calling the function
start_game()
clear_screen()
