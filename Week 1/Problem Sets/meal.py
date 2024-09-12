# Defines the main function of the program.

def main():

    # Asks the user what time is it?

    time = input("What time is it? ")
    converted = convert(time)

    # Checks if the returned float value matches any
    # of the values and prints the appropriate response.
    
    if converted >=7 and converted <= 8:
        print("Breakfast Time")
    elif converted >= 12 and converted <= 13:
        print("Lunch Time")
    elif converted >= 18 and converted <= 19:
        print("Dinner Time")

# Converts the time (string) in 24-hour format into a float.

def convert(time):

    # Splits the time into separate values (.split(":"))

    hours, minutes = time.split(":")

    # Converts and returns the string input into a float

    hours = float(hours) + (float(minutes) / 60)
    return hours

# Runs the program

main()

# DO NOT TOUCH

if __name__ == "__main__":
    main()