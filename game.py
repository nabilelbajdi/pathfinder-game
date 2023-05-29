import os
import sys
import time
import random


# Function to give a typewriter effect for print statements
def typewriter_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Typing speed
    print() # This will move to the next line after printing the whole text

# Function for clearing the terminal
def clear_screen():
    if os.name == 'posix':  # For UNIX/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        # For unsupported operating systems, it will do nothing.
        pass


# Prints an overview of the game when starting the application
def start_game():
    typewriter_print("Welcome to Pathfinder!")
    typewriter_print("Prepare yourself for an immersive text-based adventure that will take you on a journey.")
    typewriter_print("Throughout the game, you will face choices that shape your destiny.")
    typewriter_print("Your decisions will determine the outcome of your adventure, so choose wisely!")
    input("Press Enter when you are ready ")


# Act 1: The Mysterious Island
def act1():
    typewriter_print("Act 1: The Mysterious Island\n")
    typewriter_print("After a stormy voyage in the atlantic oceaen, you find yourself stranded on a deserted island.")
    typewriter_print("As you explore the island, you find three different paths ahead of you:")
    typewriter_print("1. A dense and mysterious forest, with tall trees, an earthy scent and a distans sound of wildlife.")
    typewriter_print("2. A breathtaking beach with soft, golden sands. The soun of the gentle waves fill you with tranquility.")
    typewriter_print("3. An entrance to an ancient and ominous cave, shrouded in haunting silence yet filled with muystery.")

    # Prompt the player to choose a path
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


# Act 2: The Magical Creature - Forest Path
def act2_forest():
    typewriter_print("Act 2: The Magical Creature\n")
    typewriter_print("You enter the enchanted forest and encounter a mythical creature known as the Moon Wolf.")
    typewriter_print("The Moon Wolf possesses a powerful artifact but needs your help to heal its injuries.")
    typewriter_print("To heal the Moon Wolf and earn the its trust, you must embark on a quest to collect a luminescent mushroom.")
    clear_screen()

    # Call the quest function
    moon_wolf_quest()

# Moon Wolf Quest function, as part of Act 2: The Magical Creature
def moon_wolf_quest():
    typewriter_print("The Moon Wolf provides you with a clue to find the luminescent mushroom:")
    typewriter_print("Listen closely, for the path to the mushroom lies in the moon's gentle glow.")
    typewriter_print("As you embark on your journey to find the mushroom, you find yourself at a crossroad, with two paths before you.")
    typewriter_print("One path is illuminated by a soft, silver light, while the other is engulfed in darkness.")

    while True:
        path_choice = input("Which path do you choose? (illuminated/dark) ")

        if path_choice == "illuminated":
            clear_screen()
            typewriter_print("You follow the illuminated path, guided by the moon's gentle glow.")
            typewriter_print("As you venture deeper into the forest, you suddenly hear a familiar howl.")
            typewriter_print("Without realizing, you circled back to the Moon Wolf.")
            typewriter_print("The Moon Wolf thanks you for your effort and rewards you with the luminescent mushroom.")
            typewriter_print("Congratulations! You have completed the quest and obtained the luminescent mushroom.")
            time.sleep(1)  # Slight pause before transitioning
            clear_screen()
            # Transition to Act 3 for the forest path
            act3_forest()
            break
        elif path_choice == "dark":
            clear_screen()
            typewriter_print("You choose the dark path, but it leads you into a treacherous maze of thorns and dangers.")
            typewriter_print("Unable to find your way out, you succumb to the darkness.")
            typewriter_print("Game over.")
            # UNFINISHED: Should game end here or allow option to restart?
        else:
            clear_screen()
            typewriter_print("Invalid choice. Please choose either 'illuminated' or 'dark'.")


# Act 3: The Final Confrontation - Forest Path
def act3_forest():
    typewriter_print("Act 3: The Final Chapter\n")
    # UNFINISHED: Act 3 forest story and gameplay


# Act 2: The Secret Message - Beach Path
def act2_beach():
    typewriter_print("Act 2: The Secret Message\n")
    typewriter_print("You follow the path that leads to the beach, drawn to the soothing sound of the waves.")
    typewriter_print("You decide to take a swim in the crystal clear blue water.")
    typewriter_print("As you are swimming, you discover a glass bottle in the water, containing a rolled piece of paper inside.")
    typewriter_print("With intrigue, you unroll the paper to reveal a riddle:")
    typewriter_print("'I can be gentle or brutal, shape landscapes or quench your thirst, and I'm essential for all life on Earth—what am I?'")

    # Riddle answer and reward keyword to advance Act 3: The Water Portal
    riddle_answer = "water"
    reward_keyword = "balance"

    while True:
        user_answer = input("Can you solve the riddle? Enter your answer: ")

        if user_answer.lower() == riddle_answer:
            clear_screen()
            typewriter_print("Congratulations! You've solved the riddle!")
            typewriter_print("As you utter the answer, the water before you begins to stir.")
            typewriter_print("You watch in awe as the water forms into sparkling letters, spelling out 'balance'.")
            typewriter_print("The water then recedes, revealing a magical portal shimmering in the distance.")
            typewriter_print("Before entering the portal, you take a moment to memorize the word 'balance'.")
            time.sleep(5) # Pause to remember the word needed for act 3
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
                typewriter_print("Game Over")
                sys.exit(0) # Quit game (alternatively ask player to retry)


# Act 3: The Water Portal - Beach Path
def act3_beach(reward_keyword):
    typewriter_print("Act 3: The Water Portal\n")
    # UNFINISHED: Act 3 beach story and gamepley


# Act 2: The Hidden Artifact - Cave Path
def act2_cave():
    typewriter_print("Act 2: The Hidden Artifact\n")
    typewriter_print("As you delve deeper into the dark cave, your eyes catch a glimpse of some strange scribbled words on the wall.")
    typewriter_print("The letters are scribbled and seem to form an anagram. There is a hidden message waiting to be deciphered.")

    # The deciphered word
    word = "SECRET"
    
    while True:
        scrambled_word = "".join(random.sample(word, len(word)))  # Randomly shuffle the letters
        typewriter_print("Scrambled word: " + scrambled_word)
        
        choice = input("Enter the word to decipher it, or type 'give up' to exit: ")
        clear_screen()

        if choice.lower() == word.lower():
            typewriter_print("The scribbled words glow with an ethereal blue light, revealing a hidden entrance.")
            typewriter_print("You confidently step through the entrance, ready for what lies ahead.")
            time.sleep(2)
            clear_screen()
            act3_cave()
            break
        
        if choice.lower() == "give up":
            clear_screen()
            typewriter_print("Having given up on deciphering the code, you retreat to the cave entrance.")
            typewriter_print("To your surprise, the entrance is closed, leaving you trapped and doomed to perish in the depths.")
            typewriter_print("Game Over")

            sys.exit(0) # Quit game (alternatively ask player to retry)

        typewriter_print("That is not the correct word. Try again.")

# Act 3: The Final Confrontation - Cave Path
def act3_cave():
    typewriter_print("Act 3: The Final Confrontation\n")
    # UNFINISHED: Act 3 cave story and gameplay


# Calling the functions
start_game()
clear_screen()
act1()
