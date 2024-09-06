# The requests library will need to be installed using `python -m pip install requests` in your terminal window.
# This library allows the programme to send HTTP requests very easily. Requests can be used to send and receive data
# websites by providing a uniform interface for both GET and POST requests. This programme uses the requests library to
# make HTTP GET requests to an api called RPS-101
import requests

# Standard python library packages
import random
import copy
import time
import math


def main():
    start_animation()  # Getting that string slicing in!
    game_intro()  # Welcome and about script on console for user
    import_objects = import_game_objects()  # returns 101 objects from RPS-101 API
    user_selection_list = random_ten_game(import_objects)  # returns 10 random game objects for the user to choose from
    user_choices = set_game_objects(user_selection_list)
    play_user_game(user_choices)


# Retro-styled animation using string slicing
def start_animation():
    title_string = "Rock Paper Scissors...And More!"
    string_length = len(title_string)
    left_pointer = int(math.floor(len(title_string) / 2))
    right_pointer = left_pointer + 1
    while left_pointer >= -1 and right_pointer <= string_length:
        try:
            left_padding = left_pointer * " "
            print(f"{left_padding}{title_string[left_pointer: right_pointer]}")
            left_pointer -= 1
            right_pointer += 1
            time.sleep(0.25)
        except IndexError:
            break


# User welcome and explanation of the game
def game_intro():
    big_bang_theory_link = "https://www.youtube.com/watch?v=x5Q6-wMx-K8"
    print(f"\n\nWelcome to Rock Paper Scissors...And More.\n"
          f"\nHave you seen that episode of the Big Bang Theory\n"
          f"where Sheldon explains how to play\n"
          f"Rock-Paper-Scissors-Lizard-Spock?\n"
          f"\nNo? Really!!\n"
          f"\nWell here's the YouTube...{big_bang_theory_link}\n"
          f"\nOk, so now it's your turn. The API Rock-Paper-Scissors 101 offers you\n"
          f"the chance to extend the original game with a choice of 101 objects.\n"
          f"\nIn this game, you get to pick TWO new objects to add to\n"
          f"the basic game of Rock, Paper, Scissors. Once you've picked them,\n"
          f"you get to spar with your computer at your very own game of\n"
          f"Rock-Paper-Scissors...And More\n"
          f"\nAre you ready to start?\n"
          f"Put your cursor on the empty row below and press RETURN"
          f""
          f"...Enjoy!!")
    input("")


# Get full set of possible game options through an API call
def import_game_objects():
    endpoint = "https://rps101.pythonanywhere.com/api/v1/objects/all"
    data = make_api_call(endpoint)  # calls api for all objects available from rps-101
    return data


# Game version that generates ten random objects for the user to choose from. Other variations of this game function
# could be included to offer different game versions to the user.
def random_ten_game(api_object_list):
    # make a copy of the object list to keep original object list reusable
    api_object_list_copy = copy.deepcopy(api_object_list)
    # remove 'rock', 'paper' and 'scissors' because they will always be included in the user's game
    rps_objects = ['Rock', 'Paper', 'Scissors']
    for item in rps_objects:
        if item in api_object_list_copy:
            api_object_list_copy.remove(item)
    # get 10 objects from the 101 api objects at random
    object_list = []
    while len(object_list) < 10:
        random_num = random.randint(1, 98)  # Reduced length of 98 due to removal of 3 objects (rps_objects)
        random_object = api_object_list_copy[random_num - 1]  # Change random_num to an index position
        # check for repeats
        if random_object.lower() not in object_list:
            object_list.append(random_object.lower())
    return object_list


# Returns the user's two selected objects
def set_game_objects(user_selection_list):
    user_choices = []
    print("Ok, let's generate your choices...")
    print(f"Here is a random selection of the new objects that you will\n"
          f"be able to add to your Rock Paper Scissors game:\n")
    ask_about_superpowers(user_selection_list)

    while len(user_choices) < 2:
        choice = get_user_choice(user_selection_list)
        if choice in user_selection_list:
            user_choices.append(choice)
            user_selection_list.remove(choice)

    return user_choices


# User selects the TWO objects for their game
def get_user_choice(list_of_choices):
    user_choice = input("Choose one object you would like to add: ")
    if user_choice in list_of_choices:
        return user_choice.lower()
    else:
        print("Invalid choice. Please choose from the available options.")


# Show user the objects they can choose from and give them the chance to check out an object's powers
def ask_about_superpowers(user_selection_list):
    print(f"\n{user_selection_list}")
    object_power_to_check = input("\nYou can check to see an object's superpowers.\n"
                                  "Enter one object name here (otherwise, press RETURN/ENTER to make your choices): \n")
    if object_power_to_check:
        power_check_for_errors(object_power_to_check, user_selection_list)
    else:
        return 0


# Validity check on objects selected for win condition checking through the API
def power_check_for_errors(object_power_to_check, user_selection_list):
    if is_alpha_or_dot_or_space(object_power_to_check):
        if object_power_to_check.lower() in user_selection_list:
            fetch_and_process_results(object_power_to_check, user_selection_list)
            ask_about_superpowers(user_selection_list)
        elif object_power_to_check != "" and object_power_to_check.lower() not in user_selection_list:
            print("Invalid choice. Please choose from the available options.")
            ask_about_superpowers(user_selection_list)
    else:
        print("Invalid choice. Please choose from the available options.")
        ask_about_superpowers(user_selection_list)


# Accept user inputs if all string chars are letters, dots or spaces (eg must allow 't.v.' and 'video game')
def is_alpha_or_dot_or_space(input_string):
    return all(char.isalpha() or char == "." or char == " " for char in input_string)


# Improve user experience by making API calls to get win conditions for user-selected objects
def fetch_and_process_results(object_power_check, user_selection_list):
    endpoint = f"https://rps101.pythonanywhere.com/api/v1/objects/{object_power_check}"
    powers_data = make_api_call(endpoint)  # api call for all win conditions for selected object
    winning_powers_data = powers_data["winning outcomes"]  # returns a list of lists [[a, b], [c, d]...]

    # create copy of user_selection_list so can manipulate without changing original
    user_selection_list_copy = copy.deepcopy(user_selection_list)
    object_power_check = object_power_check.lower()
    # add rps to get full set of results of an object's powers for this game
    user_selection_list_copy = user_selection_list_copy + ['rock', 'paper', 'scissors']
    # remove query object from list of objects against which the win conditions will be checked
    user_selection_list_copy.remove(object_power_check.lower())

    # check for wins (ie objects in the winning conditions and in the user selection list)
    print(f"\nWins for {object_power_check.capitalize()}:")
    for win in winning_powers_data:  # each list_item format is ['a', 'b']
        if win[1].lower() in user_selection_list_copy:  # a win
            user_selection_list_copy.remove(win[1].lower())
            print(f"{object_power_check.capitalize()} {win[0]} {win[1]}")

    # check for losses (ie remaining objects in the user selection list copy that aren't in the winning conditions)
    print(f"\nLosses for {object_power_check}:")
    for item in user_selection_list_copy:
        print(f"{object_power_check.capitalize()} loses against {item.capitalize()}")


# Runs game based on user's selected game objects
def play_user_game(user_choices):
    # single list of game choices
    game_choices = ['rock', 'paper', 'scissors'] + user_choices
    print(f"\nGreat choices!\n"
          f"You are about to play your computer at\n"
          f"Rock, Paper, Scissors, {user_choices[0].capitalize()}, {user_choices[1].capitalize()}\n")
    input(f"To start the countdown, press RETURN/ENTER")
    countdown()
    # Get user choice and determine winner
    while True:
        user_choice = input(
            f"Enter your choice (rock, paper, scissors, {user_choices[0].lower()}, {user_choices[1].lower()}): ")
        if user_choice.lower() in game_choices:
            computer_choice = random.choice(game_choices)
            print(f"\nYou chose: {user_choice.capitalize()}")
            print(f"Computer chose: {computer_choice.capitalize()}")
            print(f"Checking to see who wins the game...\n")
            result = determine_winner(user_choice, computer_choice)
            print_result(result, user_choices)
            break
        else:
            print("Invalid choice. Please choose from the available options.")


# Timer at start of game
def countdown():
    print("Three")
    time.sleep(1)
    print("Two")
    time.sleep(1)
    print("One")
    time.sleep(1)


# Call on API to determine game outcomes
def determine_winner(user_choice, computer_choice):
    endpoint = f"https://rps101.pythonanywhere.com/api/v1/match?object_one={user_choice}&object_two={computer_choice}"
    data = make_api_call(endpoint)  # calls for results based on user and computer choices

    if data["winner"].lower() == user_choice:
        game_result = f'\nCongratulations, you won!\n'\
                      f'{data["winner"]} {data["outcome"]} {data["loser"]}\n'
    elif data["loser"].lower() == user_choice:
        game_result = f'\nSorry, you did not win this time.\n'\
                      f'{data["winner"]} {data["outcome"]} {data["loser"]}\n'
    else:  # Case when user_choice == computer_choice
        game_result = f'It is a draw. You both chose {user_choice.capitalize()}'
    return game_result


# User elects to continue to play or stop
def print_result(result, user_choices):
    write_result_to_file(result)
    print(result)
    print("The outcome of your game has been saved in the 'game_results.txt' file.")
    while True:
        replay_input = input("Would you like to play again? y/n: \n")
        if replay_input.lower() == "y":
            play_user_game(user_choices)
            break
        elif replay_input.lower() == "n":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Enter y or n")


# Reusable function for all api calls
def make_api_call(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # raise http error if required
        return response.json()
    except requests.exceptions.RequestException as e:
        print("An error occurred: ", e)
        return None


# Record game result
def write_result_to_file(result):
    with open("game_result.txt", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()
