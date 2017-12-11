#Sherman_Bell
#CTI_110
#M6T1_Kilometer
#8_Nov_2017

# Write a program that asks the user to enter a distance in kilometers, and then converts that distance into miles.
# This is the conversion formula ( Miles = Kilometers * 0.6214)
# You should create two functions for this program: 1( A main() function , and)   2( A show_miles () function that takes km as a parameter, converts to miles, and prints the answers

def askUserForKilometers ():
        userKilometers = float ( input( " Please enter the distance in Kilometers:  " ) )
        return userKilometers
def convertKilometerstomiles( userKilometers ) :
        miles = userKilometers* 0.6214
        return miles


def main() :
        userKilometersTyped = askUserForKilometers ()
        convertedMiles = convertKilometerstomiles( userKilometersTyped )

        print( userKilometersTyped, " You enter: ")
        print()
        print( format( convertedMiles, ".2f" ), " Converted to miles is")
           
main()
