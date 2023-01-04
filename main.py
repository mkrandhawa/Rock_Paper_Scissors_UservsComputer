##################################### ROCK PAPER SCISSORS - USER VS COMPUTER ###########################################
import random


def play_game(rounds):
    computer_points = 0  # stores computer's points
    user_points = 0  # stores user's points
    count = 0  # used for iteration
    rps_list = ['rock', 'paper', 'scissors']  # this list will be used by the computer
    letters = ['r', 'p', 's']  # this list will be used to check the user input format
    while count < rounds:
        i = True
        comp_selection = random.choice(rps_list)  # selecting a random element from the list
        user_selection = input("Rock (R), Paper (P), or Scissors (S)? ")  # asking for the user input
        user_selection = user_selection.lower()  # conversion to lower letters
        while i:
            if user_selection not in letters:  # validating the user input
                print(f'{user_selection} is not a valid character! Please try again')
                user_selection = input("Rock (R), Paper (P), or Scissors (S)? ")
            else:
                i = False
        # this if condition will be used to check all the possible cases:
        # E.G. User = Paper Computer = Rock the point will be given to the user
        if ((comp_selection == 'rock' and user_selection == "p") or
                (comp_selection == "paper" and user_selection == 's') or
                (comp_selection == "scissors" and user_selection == 'r')):
            user_points += 1
            print(f'The score after round {count + 1} is : You : {user_points}   Computer: {computer_points}')
            print("")
        elif ((comp_selection == 'rock' and user_selection == "r") or
              (comp_selection == "paper" and user_selection == 'p') or
              (comp_selection == "scissors" and user_selection == 's')):
            print(f"You both chose same elements! Which is {comp_selection} No score given!")
            print(f'The score after round {count + 1} is : You : {user_points}   Computer: {computer_points}')
            print("")

        elif ((comp_selection == 'paper' and user_selection == "r") or
              (comp_selection == "scissors" and user_selection == 'p') or
              (comp_selection == "rock" and user_selection == 's')):
            computer_points += 1
            print(f'The score after round {count + 1} is: You : {user_points}    Computer: {computer_points}')
            print("")
        count += 1
    if computer_points > user_points:
        print("Computer won the game! Better luck next time")
    elif user_points > computer_points:
        print("You won the game! Well done!")
    else:
        print("It is a tie!")


try:
    rounds_num = int(input("How many rounds do you want to play? "))
    play_game(rounds_num)  # recalling the function
except ValueError:
    print("The number of rounds should be an integer!")
