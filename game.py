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
            clear_screen()
            act2_forest()
            break
        elif choice == "beach":
            clear_screen()
            act2_beach()
            break
        elif choice == "cave":
            clear_screen()
            act2_cave()
            break
        else:
            clear_screen()
            print("Invalid choice. Please choose either 'forest', 'beach' or 'cave'.")

def act2_forest():
    typewriter_print("Act 2: The Magical Creature\n")
    typewriter_print("You enter the enchanted forest and encounter a mythical creature known as the Moon Wolf.")
    typewriter_print("The Moon Wolf possesses a powerful artifact but needs your help to heal its injured companion.")
    typewriter_print("To heal the companion and earn the Moon Wolf's trust, you must embark on a quest to collect a luminescent mushroom.")

    # Call the quest function
    moon_wolf_quest()

def moon_wolf_quest():
    typewriter_print("The Moon Wolf provides you with a clue to find the luminescent mushroom:")
    typewriter_print("Listen closely, for the path to the mushroom lies in the moon's gentle glow.")
    typewriter_print("As you embark on your journey to find the mushroom, you find yourself at a crossroad, with two paths before you.")
    typewriter_print("One path is illuminated by a soft, silver light, while the other is engulfed in darkness.")

    # Prompt the player to choose a path
    path_choice = input("Which path do you choose? (illuminated/dark) ")

    if path_choice == "illuminated":
        clear_screen()
        typewriter_print("You follow the illuminated path, guided by the moon's gentle glow.")
        typewriter_print("As you venture deeper into the forest, you suddenly hear a familiar howl.")
        typewriter_print("You realize that you have unknowingly circled back to the Moon Wolf.")
        typewriter_print("The Moon Wolf acknowledges your efforts and rewards you with the luminescent mushroom.")
        typewriter_print("Congratulations! You have completed the quest and obtained the luminescent mushroom.")
        time.sleep(1)  # Slight pause before transitioning
        clear_screen()
        # Transition to Act 3 for the forest story
        act3_forest()

    elif path_choice == "dark":
        clear_screen()
        typewriter_print("You choose the dark path, but it leads you into a treacherous maze of thorns and dangers.")
        typewriter_print("Unable to find your way out, you succumb to the darkness.")
        typewriter_print("Game over.")
        # Should game end here or allow option to restart?

    else:
        clear_screen()
        typewriter_print("Invalid choice. Please choose either 'illuminated' or 'dark'.")

# Act 3: The Final Confrontation
def act3_forest():
    typewriter_print("Act 3: The Final Chapter\n")
    # Act 3 forest story and gameplay

def act2_beach():
    typewriter_print("Act 2: The Secret Message\n")
    typewriter_print("You follow the path that leads to the beach, drawn to the soothing sound of crashing waves.")
    typewriter_print("As you walk along the sandy shore, a glimmer catches your eye.")
    typewriter_print("You discover a small, glass bottle washed up on the beach, containing a tightly rolled piece of paper inside.")
    typewriter_print("With intrigue, you unroll the paper to reveal a riddle:")
    typewriter_print("'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'")

    # Riddle answer and reward keyword
    riddle_answer = "echo"
    reward_keyword = "serenity"

    while True:
        user_answer = input("Can you solve the riddle? Enter your answer: ")

        if user_answer.lower() == riddle_answer:
            clear_screen()
            typewriter_print("Congratulations! You've solved the riddle!")
            typewriter_print("As the answer escapes your lips, the water before you begins to stir.")
            typewriter_print("You watch in awe as the water forms into sparkling letters, spelling out 'serenity'.")
            typewriter_print("The water then recedes, revealing a magical portal shimmering in the distance.")
            typewriter_print("Before entering the portal, you take a moment to memorize the word 'serenity'.")
            time.sleep(3)
            clear_screen()
            act3_beach(reward_keyword)
            break

        else:
            clear_screen()
            typewriter_print("That's not the correct answer.")
            choice = input("Do you want to try again? (yes/no) ")

            while choice.lower() not in ["yes", "no"]:
                clear_screen()
                typewriter_print("Invalid choice. Please enter 'yes' or 'no'.")
                choice = input("Do you want to try again? (yes/no) ")

            if choice.lower() == "no":
                clear_screen()
                typewriter_print("You decide not to attempt the riddle any further.")
                typewriter_print("As you continue to relax in the ocean, a massive sea creature rises from the depths and devours you.")
                typewriter_print("Your adventure ends here, consumed by the unknown perils of the deep sea.")
                sys.exit(0)

def act3_beach(reward_keyword):
    typewriter_print("Act 3: The Water Portal\n")
    # Act 3 beach story and gamepley


def act2_cave():
    typewriter_print("Act 2: The Hidden Artifact\n")
    # Cave story

# Calling the functions
start_game()
clear_screen()
act1()
