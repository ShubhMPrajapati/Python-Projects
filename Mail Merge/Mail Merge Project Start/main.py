with open("./Input/Letters/starting_letter.txt") as starting_letter:
    read = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    for name in names:
        text = read.replace("[name]", name.strip())
        with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w") as file:
            file.write(text)
