#  functions go here
def yes_no(question):
    """Checks users enter yes / no"""

    while True:
        response = input(question).lower()

        """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        elif response == "xxx":
            break
        else:
            print("please enter yes / no")


def instructions():
    """Print instructions"""

    print("""
*** Instructions ***
 Roll the dice and try to win!
    """)


# Main routine


# ask the user if they want instructions (check they say / no)
want_instructions = yes_no("Do you want to see the instructions?")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
