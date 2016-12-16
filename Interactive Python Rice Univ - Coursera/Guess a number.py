Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui

number_of_guesses = 7
secret_number = 0
limit = 100

def new_game():
    global number_of_guesses, limit
    number_of_guesses = 7
    print "Guess a number"
    print"Please enter a number between 0 and %d" %(limit)
    print"You have %d tries remaining\n" %(number_of_guesses)
    

# define event handlers for control panel
def range100():
    global secret_number
    secret_number = random.randrange(0, 100)
    new_game()



def range1000():
    global secret_number, limit
    limit = 1000
    secret_number = random.randrange(0, 1000)
    new_game()

    
def input_guess(guess):
    try:
        guess_int = int(guess)
        global number_of_guesses
        if number_of_guesses > 0:
            if guess_int < secret_number:
                number_of_guesses -= 1
                print 'Guess was', guess
                print 'Number of guesses remaining is', number_of_guesses
                print 'Higher!\n'
            elif guess_int > secret_number:
                number_of_guesses -= 1
                print 'Guess was', guess
                print 'Number of guesses remaining is', number_of_guesses
                print 'Lower!\n'
            else:
                number_of_guesses -= 1
                print 'Guess was', guess
                print 'Number of guesses remaining is', number_of_guesses
                print 'Correct!\n'
        else:
            print 'Game over'
            print 'Number is:', secret_number
    except:
        error_guess = guess
        print "%s is not a number, please enter a number\n" %(error_guess)
        new_game
    
frame = simplegui.create_frame("Guessing Game", 300, 200)
player_guess = frame.add_input('Enter your guess', input_guess, 100)

# register event handlers for control elements and start frame
inp1 = frame.add_button('0-100', range100, 100)
inp2 = frame.add_button('0-1000', range1000, 100)


# call new_game 
new_game()


