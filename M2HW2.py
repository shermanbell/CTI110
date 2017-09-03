# CTI-110
# M2HW2 TIP, TAX, AND TOTAL
# SHERMAN BELL
# 3_SEPT_2017

# Write a progam that calculates the toatal cost of a meal purchased at a restaurant.
# Program shoul ask the user to enter the cost of meal on menu
# Calculate the amout of the tip and amount for sales tax
# Display both of these amounts as well as the total cost of the meal.
# Assume 18% is tip
# Assume 7% is sales tax

mealCost = float( input ( "Enter meal cost here: " ) )
tip = 0.18 * mealCost
salesTax = 0.07 * mealCost
total = mealCost + tip + salesTax
print ( "Price of Meal : $" + format ( mealCost, ",.2f"), "Tip: $" + \
        format ( tip, ",.2f"), "Sales Tax: $ " + format ( salesTax, " ,.2f"), \
        " All Charges: $ " + format (total, " ,.2f" ))

                           

        


