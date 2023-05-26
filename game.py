# Prints welcome message and descsription of the game when starting it
import os

def start_game():
    print("Welcome to the Text Adventure Game! This is an interactive text-based adventure game that will take you through a journey.")
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
