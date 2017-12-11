#Sherman_Bell
#CTI_110
#M6T2_Feet to inches
#8_Nov_2017

#  A brief description of the project: program that converts feet to inches
# 8_Nov2017
# CTI-110 M6T2_FeetToInches
# Sherman Bell

# Write a program using a value-returning function for this assigment.
# Program that asks the user to enter a distance in feet, and prints that same distance in inches
# Conversion formula ( inches= feet * 12)
# You shoud create two functions for this program
# Main() function that calls the next functon and prints the answer
# A feet to inches() function that asks the user to enter a distance in feet, calculates the distance in inches, and returens that value

def feetToinches ( userFeet ) :
        inches = ( userFeet / 1) * 12
        return inches
def main():
        userFeet = float( input( " Please enter the number of feet: ") )
        inches = feetToinches ( userFeet )
        print ()
        print ( userFeet , " Feet (s) You enter ")
        print()
        print( format( inches, " .2f" ) , "inches")
        


main()
