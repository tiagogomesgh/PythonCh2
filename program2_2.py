### Tiago Gomes - 2375703
### COP1000 - #1284
### program2_2.py

### PSEUDOCODE
### PROMPT the user to enter the # of hours to convert.
### STORE the input as an INT
### CALCULATE the total # of days and remaining hours.
### PRINT the results in the desired format.


def main () :
    ### PROMPT for input and STORE as integer.
    hours = int(input("What is the number of hours to convert to days and hours? "))
    ### CALCULATE total days and rounds down to the nearest whole number.
    days = hours // 24
    ### CALCULATE remaining hours using modulus operator.
    remainingHours = hours % 24
    ### PRINT results in desired format.
    print(f'{hours} hours is equivalent to {days} days and {remainingHours} hours')
main ()
