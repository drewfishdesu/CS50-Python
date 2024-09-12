# Defines the main function of the program

def main():
        while True:

                # Prints an empty line.

                print("\n")

                # Asks the user for the crit values of the artifact.

                crit_damage = cd_to_float(input("How much crit damage does your artifact have? "))
                crit_rate = cr_to_float(input("How much crit rate does your artifact have? "))
                print("\n")

                # Calculates the crit value of the artifact.

                crit_value = crit_damage + crit_rate * 2
                
                # Prints the crit value of the artifact.

                print("Your artifact has",crit_value,"CV.")
                print("\n")

                # Asks the user if they want to check another artifact.
                again = input("Do you want to check the crit value of another artifact? [Yes/No] ").strip().lower()
                if again != "yes":
                        break


# Converts the crit values to float values.

def cd_to_float(x):
        cd = (x)
        return float(cd)
def cr_to_float(y):
        cr = (y)
        return float(cr)
                
main()
