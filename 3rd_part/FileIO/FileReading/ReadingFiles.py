def open_file():
    file = open('story.txt')
    print(file.read())
    file.seek(0)  # places the cursor to home position
    print(file.readlines())  # places all lines in a list of lines
    file.close()


def open_file_with():
    with open('story.txt') as file:
        text = file.read()
    print(text)
    print(file.closed)

# With blocks are better 'cause it automatically closes the file after


