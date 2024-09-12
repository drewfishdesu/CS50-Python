# Defines the main function of the program.

def main():

    # Asks the user for a file name.

    print("\n")
    name = input("File Name: ").lower().casefold().strip()

    # Matches the file to known file types:

    if name.endswith(".gif"):
        print("image/gif")
    elif name.endswith(".jpg"):
        print("image/jpeg")
    elif name.endswith(".jpeg"):
        print("image/jpeg")
    elif name.endswith(".png"):
        print("image/png")
    elif name.endswith(".pdf"):
        print("application/pdf")
    elif name.endswith(".zip"):
        print("application/zip")
    elif name.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

# Runs the program.

main()