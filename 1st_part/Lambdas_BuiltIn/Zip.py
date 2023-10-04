midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

final_grades = dict(                 # {dan: 98, ang: 91, kate: 78}
    zip(
        students,                    # ((dan, 98),(ang, 91),(kate,78))
        map(lambda pair: max(pair),  # (98, 91, 78)
            zip(midterms, finals))   # ((80,98),(91,89),(78,53))
    )
)

print(final_grades)
