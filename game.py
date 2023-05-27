import os
import sys
import time

# Function to give a typewriter effect for print statements
def typewriter_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)  # Typing speed
    print()  # This will move to the next line after printing the whole text

def clear_screen():
    # Clear the terminal screen after the welcome message above
    if os.name == 'posix':  # For UNIX/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        # For unsupported operating systems, it will do nothing.
        pass

# Prints welcome message and instructions for the game when starting it
def start_game():
    typewriter_print("Welcome to the Text Adventure Game! This is an interactive text-based adventure game that will take you through a journey.")
    typewriter_print("You will be prompoted with options that will dictate your journey. ")
    input("Press Enter to start the game ")

# Act 1: The Mysterious Island
def act1():
    typewriter_print("Act 1: The Mysterious Island\n")
    typewriter_print("After setting sail on a voyage across the ocean, you find yourself stranded on a deserted island after a horrible storm.")
    typewriter_print("As you explore the island, you find three different paths ahead of you:")
    typewriter_print("1. A dense and mysterious forest, with tall green trees casting long shadows. You can feel the thick air, it has an earthy scent and the distant sound of wildlife.")
    typewriter_print("2. A breathtaking beach with soft, golden sands, carrying the breeze with the scent of ocean. The gentle waves create a soothing melody filling you with tranquility.")
    typewriter_print("3. An entrance to what looks to be an ancient and ominous cave. Its haunting silence echoes as you approach it, yet still gives a sense of mystery and intrigue.")


    while True:
        choice = input("Which path do you choose? (forest/beach/cave) ")

        if choice == "forest":
            act2_forest()
            break
        elif choice == "beach":
            act2_beach()
            break
        elif choice == "cave":
            act2_cave()
            break
        else:
            print("Invalid choice. Please type one of the following: forest/beach/cave")

def act2_forest():
    typewriter_print("Act 2: The Magical Creature\n")
    # Forest story

def act2_beach():
    typewriter_print("Act 2: The Secret Message\n")
    # Beach story

def act2_cave():
    typewriter_print("Act 2: The Hidden Artifact\n")
    # Cave story

# Calling the functions
start_game()
clear_screen()
act1()
