#CTI_110
#M3HW2_Software_Sales
#SHERMAN_BELL
#9_OCT_2017

# Writ a program that asks the user to enter the number of packages purchased
# A software company sells a package that retails for $99
# They offer bulk discounts for volume purchases
# Quantity of 10-19 are 10% discount
# Quantity of 20-29 are 20% discount
# Quantity of 50-99 are 30% discount
# Quantity of 100 or more 40% discount
#The program should then displan the amount of the discount if any and the total purchase cost with discount applied


userNumberofPackages = int( input( "Please enter the number of packages you would like to purchase: ") )
packagePrice = 99
if userNumberofPackages < 10:
    discount = 0
elif userNumberofPackages < 20:
    discount  = 0.10
elif userNumberofPackages < 30:
    discount = 0.20
elif userNumberofPackages <100:
    discount = 0.30
else:
    discount = 0.40

subTotal = userNumberofPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "Amount of discount: $ " +  format( discountAmount, " ,.2f" ) )
print( "Total amount: $ " + format( total, ",.2f") )
print( " Buy more save more")
