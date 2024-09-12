# Defines the main function of the program.

def main():
    name = input("What's your name? ")

    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    else:
        print("Who?")

main()