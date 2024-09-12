# Defines the main function of the program

def main():

    # Prints a blank space.

    print("\n")

    # Asks the user for input.

    life = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()

    # Checks if the answer is correct, then, prints yes. Otherwise, prints, no.

    if life == "42" or life == "forty-two" or life == "forty two":
        print("Yes")
    else:
        print("No")

main()
