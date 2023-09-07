str1 = ""


def speak(string="dog"):
    if string == "pig":
        return "oink"
    if string == "duck":
        return "quack"
    if string == "cat":
        return "meow"
    if string == "dog":
        return "woof"
    else:
        return "?"


print(speak(str1))
