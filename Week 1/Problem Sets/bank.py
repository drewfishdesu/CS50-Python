# Defines the main function of the program

def main():
    
    # Prints an empty line

    print("\n")

    # Asks the user for an input.

    greeting = input("Greeting: ").lower().strip()

    # Checks if the input matches any of the criteria set below.

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h", 0) and greeting != "hello":
        print("$20")
    else:
        print("$100")

    # Prints an empty line

    print("\n")

# Runs the program

main()