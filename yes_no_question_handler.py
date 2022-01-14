def to_evaluator(repeat):
    while True:
        if repeat.lower().strip() == 'no':
            return True
        elif repeat.lower().strip() == 'yes':
            return False
        else:
            repeat = input("\nPlease enter a valid answer ('yes' or 'no')\nWould you like to add another place (yes/ no)? ")

while True:
    repeat = input("Would you like to add another place (yes/ no)? ")
    to_eval = to_evaluator(repeat)
    if to_eval:
        print("You have chosen 'no'")
    elif not(to_eval):
        print("You have chosen 'yes'")
