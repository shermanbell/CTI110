#CTI_110
#M3HW1_AGE_CLASSIFIER
#SHERMAN_BELL
#9_OCT_2017

# Write a progam that ask the user to enter a person's age
# If the person is 1 year old or less, he or she is an infant
# if the person is older that one year, but younger than 13 years, he or she is child
# if the person is at least 13 years old, but less than 20 years old, he or she is a teenager
# if the person is at least 20 years old, he or she is and adult

personAge = int( input( "Please enter your age here: ") )
if personAge <= 1:
    print( "He or she is an infant")
elif personAge < 13 :
    print( "He or she is a child")
elif personAge < 20 :
    print( "He or she is a teenager")
else:
    print( "He or she is an adult")
    

