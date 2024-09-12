# Defines the main function of the program.

def main():

    # Asks the user for an integer input.

    x = int(input("What's x? "))
    
    # Checks if the number has a remainder or not and determines whether or not the number is even.

    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

main()