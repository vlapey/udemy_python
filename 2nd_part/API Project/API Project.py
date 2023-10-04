from random import choice

import requests
import pyfiglet

print(pyfiglet.figlet_format("Dad Joke"))
while True:
    term = input("Let me tell you a joke! Give me a topic: \n")
    response = (requests.get(
        "https://icanhazdadjoke.com/search",
        headers={"Accept": "application/json"},
        params={"term": f"{term}"})).json()

    total_jokes = response['total_jokes']

    if total_jokes == 0:
        print(f"There's no jokes about that, try again")
        continue

    results = response['results']
    joke = choice(results)['joke']

    if total_jokes == 1:
        print(f"I've found one joke, here it is:\n{joke}\n")
        continue

    print(f"I've found {total_jokes} jokes, here's one:\n{joke}\n")
