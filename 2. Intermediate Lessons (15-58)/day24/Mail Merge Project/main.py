SUBSTITUTION_NAME = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(SUBSTITUTION_NAME, stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}_letter.txt", mode='w') as final_letters:
            final_letters.write(new_letter)