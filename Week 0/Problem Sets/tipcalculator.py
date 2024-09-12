# Defines the main function of the program.

def main():
    print("\n")
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print("\n")
    print(f"Leave ${tip:.2f}")
    print("\n")

# Converts a numerical input into a float value.

def dollars_to_float(d):
    dollar_value = (d.replace("$",""))
    return float(dollar_value)

# Converts a percentage input into a float value.

def percent_to_float(p):
   percent_value = (p.replace("%",""))
   percent_converted = float(percent_value) / 100
   return float(percent_converted)

# Executes the function

main()