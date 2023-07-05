print("How many kilometers did you run today?")
kilometers = input()
miles = float(kilometers) / 1.609
miles = round(miles, 2)
print(f"Your {kilometers}km run was {miles}mi")
