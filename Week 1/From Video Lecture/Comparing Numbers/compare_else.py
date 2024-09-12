# Defines the main function of the program

def main():

    # Defines the variables

    print("\n")
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    print("\n")

    # Commpares if the value of x is greater than or less than y
    # This is an example of a boolean expression.

    if x < y:
        print("x is less than y")

    # elif indicates "else if"

    elif x > y:
        print("x is greater than y")

    # else tells the computer to do a function if the remaining conditionals are not met.

    else:
        print("x is equal to y")
    
    # Prints a blank space

    print("\n")

main()