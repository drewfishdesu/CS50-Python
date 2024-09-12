# Defines the main function of the program

def main():

    # Defines the variables

    print("\n")
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    print("\n")

    # Commpares if the value of x is equal or not equal to y
    # This is an example of a boolean expression.

    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal to y")
        
    # Prints a blank space

    print("\n")

main()