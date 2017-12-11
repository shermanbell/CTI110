#Sherman_Bell
#CTI_110
#M5HW3_Factorial
#30_OCT_2017


# Write a program that asks the user for a nonnegative integer and then uses a loop to calculate the factorial of that number
# Display the factoral

userInteger = int( input( "Please enter a number:"))

while userInteger < 1:
        userInteger = int( input( "Please enter a positive number: "))
factorial = 1

for currentNumber in range( 1, userInteger + 1) :
        factorial = factorial * currentNumber

print()
print( " The factorial of ",userInteger, "is", factorial )


