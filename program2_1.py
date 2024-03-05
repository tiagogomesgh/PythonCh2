### Tiago Gomes - 2375703
### COP 1000 - #1284
### program2_1.py
### PSEUDOCODE
### PROMPT the user to INPUT the cost of their meal as a decimal value.
### PROMPT the user to input the tip percentage.
### STORE the tax rate of 7% in a properly named constant
### CALCULATE the dollar amounts of the tax and tip.
### ADD these values to the original cost of the meal.
### PRINT the tax amount, followed by the tip amount, and finally the total cost of the meal.

def main () :
    ### get meal cost
    mealCost = float(input("What is the total cost of the meal? "))
    ### select tip %
    tipSelection = int(input("What is the tip percentage? "))
    ### set Constant tax rate
    TAX_RATE = 0.07
    ### convert whole % into decimal value for easier calculations
    convertedTip = tipSelection * .01
    ### calculate tax
    calculatedTax = mealCost * TAX_RATE
    ### calculate tip
    calculatedTip = mealCost * convertedTip

    ### COMBINE original meal cost with calculated tip and tax values
    totalCost = mealCost + calculatedTip + calculatedTax
    ### format final response for thousands and decimal places.
    print(f'A ${mealCost:,.2f} meal with a {tipSelection}% tip and a {TAX_RATE:.0%} tax has a grand total cost of ${totalCost:,.2f}')

main ()
