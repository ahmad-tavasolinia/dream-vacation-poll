# dream_vacation.py

dream_vacation = {}
polling_active = True

while polling_active:
    user = input("Would you please tell us your name?: ")
    place = input("What is your favorite destination?: ")
    dream_vacation[user.title()] = place.title()

    question = input("Is there any other participant? (yes/no): ")
    if question.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for user, place in dream_vacation.items():
    print(f"{user} would like to visit {place}.")

