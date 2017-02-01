# "Guess the number"
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University
#
# Student: Jose L Mortola
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

secret_number = 0
lives = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global lives
    secret_number = random.randrange(0,100)
    print "Hi! Can you guess my number? Pick a number between 0 and 100."
    lives = 7


def range100():
    # button that changes the range to [0,100) and starts a new game

    global secret_number
    global lives
    secret_number = random.randrange (0,100)
    lives = 7
    print secret_number
    print "Guess a number between 0 and 100"



def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    global lives
    lives = 10
    secret_number = random.randrange (0,1000)
    print "Guess a number between 100 and 1000"

def input_guess(guess):
    # main game logic goes here
    print "Your number is " + guess
    if int(guess) == secret_number:
        print "You win, the number was " + str(secret_number)
        if secret_number > 100 and secret_number < 1000:
            range1000()

        else:
            new_game()
    elif int(guess) > secret_number:
        print "Nope, my number is lower"
        chances(secret_number)
    elif int(guess) < secret_number:
        print "Nope, my number is higher"
        chances(secret_number)

def chances (secret_name):
    global lives
    if secret_name < 100:

        for i in range(7):
            lives -= 1
            print "You have " + str(lives) + " chances left"
            break
        if lives == 0:
            print "Sorry, you lost. Game over, the number was " + str(secret_number)
            range100()


    elif secret_name < 1000 and secret_name > 100:
        for i in range(10):
            lives -= 1
            print "You have " + str(lives) + " chances left"
            break
        if lives == 0:
            print "Sorry, you lost. Game over, the number was " + str(secret_number)
            range1000()


# create frame
frame = simplegui.create_frame("Home", 100, 200)

# register event handlers for control elements and start frame
button_100 = frame.add_button("Range 0 to 100", range100, 100)
button_1000 = frame.add_button("Range 0 to 1000", range1000, 100)
button_restart = frame.add_button("Restart Game", new_game, 100)
guess = frame.add_input("Guess", input_guess, 100)

# call new_game
new_game()
frame.start()
