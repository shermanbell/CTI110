#Sherman_Bell
#CTI_110
#M5HW1_DISTANCE TRAVELED
#30_OCT_2017

# Write a program that asks the user two question:
# "The speed of the vehicle?"
#  "Number of hours it has traveled"
# The program should then display the distance that the vehicle has traveled for each hour of that time period.
# You output should be displayed in a table format.


vehicleSpeed = float( input( "What is the speed of the vehicle:")  )
hourTraveled = int( input( " Number of hours vehicle has traveled: ") )
print()
print( "Hour", "\t Distance Travled" )
for currentHour in range( 1, hourTraveled + 1):
    distanceTraveled =  vehicleSpeed * currentHour
    print( currentHour, "\t", distanceTraveled )

