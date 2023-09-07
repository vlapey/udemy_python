s = set({1, 2, 3, 4, 5, "a", "b", 23.00556})
print(s)
# common use for sets

cities = ["LA", "LA", "Kyoto", "Florence", "Santiago", "Florence", "LA"]
print(cities)
unique_cities = list(set(cities))
print(unique_cities)


set1 = set({1, 2, 3, 4, 5, 6})
set1.add(10)
set1.remove(5)
print(set1)
new_set = set1.copy()
print(new_set)
new_set.clear()
print(new_set)
