# Defines the main function of the program.

def faces():

    # Replaces the standard emoji with Unicode emojis

    text = input("What would you like to say? ").replace(":)","🙂").replace(":(","🙁")
    print(text)

# Executes the command

faces()
