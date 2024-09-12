# Defines the main function of the program.
# This version of house.py introduces the 'match' argument.

def main():
    name = input("What's your name? ")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
main()