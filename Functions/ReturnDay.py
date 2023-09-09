def return_day(number):
    if number < 1 or number > 7:
        return None
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    return days_of_week[number - 1]


number = int(input())
print(return_day(number))
