# Defines the main function of the program.

def main():

    # Prints an empty line

    print("\n")

    # Asks the user for the score

    score = int(input("Score: "))

    # Checks if the integer is within the assigned range and assign a grade
    # based on the integer's value

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

# Asks the user for the score
print("\n")

main()
