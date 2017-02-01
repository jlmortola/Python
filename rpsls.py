# Rock-paper-scissors-lizard-Spock template
# 'Introduction to Interactive Programming in Python' Course
# RICE University
#
# Student: Jose L Mortola
#
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def choice_to_number (player):
    #make player choice a number
    if player == "rock":
        return 0
    elif player == "Spock":
        return 1
    elif player == "paper":
        return 2
    elif player == "lizard":
        return 3
    elif player == "scissors":
        return 4
    else:
        return "bad input"

def number_to_name(number):
    #make number to name
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"

def rpsls (player):
    # print player choice
    print "Player chooses: " + player

    # add a the computer choice and print it
    computer_choice = random.randrange(0,4)
    print "Computer chooses: " + number_to_name(computer_choice)

    print "And the winner is:"

    # compare choices to detect winner
    if choice_to_number(player) == "bad input":
        print "Ohh, too bad. Player made a bad input, please try again."
    elif choice_to_number(player) == computer_choice:
        print "It's a tie, please try again."
    elif choice_to_number(player) %5 > computer_choice %5:
        print player + "! You win, congratulations!"
    elif choice_to_number(player) %5 < computer_choice %5:
        print number_to_name(computer_choice) + "! Computer wins this time."


rpsls ("paper")
