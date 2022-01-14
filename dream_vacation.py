def to_evaluator(repeat):
    while True:
        if repeat.lower().strip() == 'no':
            return True
        elif repeat.lower().strip() == 'yes':
            return False
        else:
            repeat = input("\nPlease enter a valid answer ('yes' or 'no')\nWould you like to add another place (yes/ no)? ")

places = []

while True:
    place = input("\nIf you could visit one place in the world, where would you go? ")
    places.append(place)
    repeat = input("Would you like to add another place (yes/ no)? ")
    to_eval = to_evaluator(repeat)
    if to_eval:
        break
    elif not(to_eval):
        continue

print("\n--- Poll Results ---")
for place in places:
    print(f'    {place}')



