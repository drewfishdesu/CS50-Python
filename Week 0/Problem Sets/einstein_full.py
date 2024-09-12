# Greets the user to the Einstein Calculator.

print("\n")
print("Welcome to the Einstein Calculator!")
print("\n")

# Defines the main function of the program.

def einstein():

    # Asks the user for any float

    number = int(input("Input any number into Einstein's magical formula, e = mc^2!\n(This is the 'm' in the formula.) "))
    
    # Calculates the number and multiplies it by the speed of light (300000000^2)

    answer = number * 300000000**2

    # Prints the answer

    print(answer)
    print("\n")
    print("The answer is ",answer,".",sep="")
    print("\n")

    # Confirms that the calculation is complete.

    print("Calculation complete.")
    print("\n")

# Runs the command

einstein() 