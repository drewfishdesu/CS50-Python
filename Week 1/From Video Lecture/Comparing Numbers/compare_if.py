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
    if x > y:
        print("x is greater than y")
    if x == y:
        print("x is equal to y")
    print("\n")

main()