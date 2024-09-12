# Defines the main function of the program.

def main():

    # Asks the user for an integer input.

    x = int(input("What's x? "))
    
    # Checks if the number has a remainder or not and determines whether or not the number is even.

    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Uses boolean values instead (True or False) instead of conditionals.
# Four lines of code in this section condensed into one line.
# Refer to parity_boolean for comparison.
# This version is even more refined, but does the same thing.

def is_even(n):
    return (n % 2 == 0)

main()