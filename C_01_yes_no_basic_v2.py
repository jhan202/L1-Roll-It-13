
#  functions go here
def yes_no(question):
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




# Main routine

want_instructions = yes_no("Do you want to see the instructions? ").lower()
want_coffee = yes_no("Do you want coffee?")

print("we done")
