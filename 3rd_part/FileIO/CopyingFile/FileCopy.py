def copy(story_txt, copy_story_txt):
    with open(story_txt) as first_file, open(copy_story_txt, "w") as second_file:
        text = first_file.read()
        second_file.write(text)


copy("dot.txt", "dot_copy.txt")  # creates dot_copy.txt with its content
