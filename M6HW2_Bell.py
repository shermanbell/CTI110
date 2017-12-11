#Sherman_Bell
#CTI_110
#M6HW2_Random Number Guessing Game
#9_Nov_2017

# Write a program that does the following
# Gernerate a random number in the range of 1 through 100. ( We'll call this "secret number")
# Ask the user to guess what the secret number is
# If the user's guess the higher thatn the secret number, the program shold tell the user "Too hig, try again"
# If the user's guess is lower than the secret number, the program should tell the user " Too low, try again"
# If the user guesses the number correctly, the program should congratulate the use! Writer whatever message you think is appropriate for the case.
# The program should then ask the user Play again? (y for yes) and (n for no).
# If the user enters"y", then the program should generate a new random number and start the game over again.
#You shold, at the minimum, use a main() function
# you might use two methods structure the program, for example main() and play_ game()
# Exta Credit
# Have the game keep track of the number of guesse the user makes,. When they guess correctly, tell the user how many guesses they used.
# You might also decide that user only gets X number of guesses per game, and the game ends in a loss if they use all guesses before they guess the number.
# You will need to test for yourself and decide what a far value for X wold be


import random

def genRandomNumber():
    randomNumber = random.randint( 1, 100 )
    return randomNumber

def askUserForNumber( message = "Guess the number: "):
    userNumber = int( input( message) )
    return userNumber

def checkUserNumber( userNumber, randomNumber ) :
    if userNumber < randomNumber:
        return "Too Low , you have"
    elif userNumber > randomNumber :
        return " Too High"
    else: 
            return " Congratulations you did it"
 

def main () :
    userCongratulated = False
    letsStart = True

while userCongratulated or letsStart:
    randomNumber = generateRandomNumber ()
    userNumber = askUserForNumber ()
    message = checkUserNumber ( userNumber , randomNumber )

    while message != " Congratulations you did it":
        print( message )
        userNumber = askUserForNumber( " Try again")
        message = checkUserNumber( userNumber, randNumber )

        print( message )
        userCongratulated = True


main()
