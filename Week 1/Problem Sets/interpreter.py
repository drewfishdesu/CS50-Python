# Defines the main function of the program.

def main():

    # Asks the user to input a mathematical expression.

    math = input("Expression: ")

    # Converts user input into variables

    x, y, z = math.split()

    # Converts the input values to floats

    float_x = float(x)
    float_z = float(z)

    # Calculates the results

    if y == "+":
        answer = float_x + float_z
        print(answer)
    elif y == "-":
        answer = float_x - float_z
        print(answer)
    elif y == "*":
        answer = float_x * float_z
        print(answer)
    elif y == "/":
        answer = float_x / float_z
        print(answer)
    else:
        print("Invalid operation.")


# Runs the program

main()