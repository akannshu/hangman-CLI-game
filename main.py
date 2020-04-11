import random_word_generator
import colord


def change_current_word_state(selected_word, current_word_state, character):
    """
        Replace _ with selected character in current_word_state, at index where
        character occurs in selected_word. Return the modified current_word_state
    """
    modified_word_state = ""

    # Iterate the selected word
    for i in range(len(selected_word)):
        # If character is missing and Selected word is equal to selected character
        if current_word_state[i] == "_" and selected_word[i] == character:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]

    return modified_word_state


def input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining):
    """
        Check if input charcater is in selected_word, if not then reduce attempts
    """
    if input_char in selected_word:
        current_word_state = change_current_word_state(selected_word, current_word_state, input_char)
    else:
        attempts_remaining -= 1
    return current_word_state, attempts_remaining


def print_current_state(current_word_state, attempts_remaining):
    """
        Print formatted word state and Attempts Remaining
    """
    colord.print_information("Current State: ", end=" ")
    for i in current_word_state:
        colord.print_information(i, end=" ")

    colord.print_warning("\tAttempts Remaining : %d" % attempts_remaining)


def check_game_status(selected_word, current_word_state, attempts_remaining):
    """
        Check if game has reached end, i.e. the player has Lost or Won
    """
    if current_word_state == selected_word:
        # Print in Green
        colord.print_sucess("You WON! :D")
        return True
    elif attempts_remaining <= 0:
        # Print in Red
        colord.print_failure("You Lost :(")
        # Print in Blue - for Information
        colord.print_information("Word was %s" % selected_word)
        return True
    return False


def play_game(attempts=5):
    """
        Main game running logic
        Select random word, and take user input for comparing
    """
    # Pick a random word
    selected_word = random_word_generator.pick_random_word()

    # Create current word state by using _ instead of characters in selected_word
    current_word_state = ""

    for i in range(len(selected_word)):
        if selected_word[i] == 'a' or selected_word[i]=='e' or selected_word[i]=='i' or selected_word[i]=='o' or selected_word[i]=='u':
            current_word_state+=selected_word[i]
        else:
            current_word_state+='_'    


    # Attempts allowed
    attempts_remaining = attempts

    # Print intial state
    print_current_state(current_word_state, attempts_remaining)

    while True:
        input_char = input("Guess a character: ")
        print()

        # Check for input charcater in selected_word, and readjust attempts remaining
        current_word_state, attempts_remaining = input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining)

        # Print current game state
        print_current_state(current_word_state, attempts_remaining)

        # Check if game has ended -> Won or Lost
        game_ended = check_game_status(selected_word, current_word_state, attempts_remaining)
        if game_ended:
            break


if __name__ == "__main__":
    play_game()
