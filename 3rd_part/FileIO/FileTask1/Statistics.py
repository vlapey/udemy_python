def statistics(filename):
    with open(filename) as file:
        lines = file.readlines()
        characters = 0
        for line in lines:
            if "\n" in line:
                characters -= 1
            characters += len(line)

        result = {"lines": len(lines),
                  "words": sum(len(line.split(" ")) for line in lines),
                  "characters": characters}
        print(lines)
        return result


print(statistics("file.txt"))
