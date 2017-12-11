#Sherman_Bell
#CTI_110
#M5HW2_Running Total
#30_OCT_2017

# Write a program that asks the user to enter a series of numbers
# It should loop, adding these numbers to a running total, until the user enters a negative number
# When a negative number is entered, the program should exit the loop
# It should not add the negative number to the total
# The program should then print the total before exiting


total = 0
userNumber = float( input( "Please enter the first number ,if number is negative progam will stop and give sum:") )

while userNumber  > - 1:
        total = total + userNumber
        userNumber = float( input( " Please enter the next number") )
print( " The sum of all the numbers is:", total)
                    
        
