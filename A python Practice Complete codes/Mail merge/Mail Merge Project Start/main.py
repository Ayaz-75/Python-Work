#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as names:
    all_names = names.readlines()

with open('Input/Letters/starting_letter.txt') as data:
    letter = data.read()
    for name in all_names:
        new_letter = letter.replace('[name]', name.strip())
        striped_name = name.strip()

        with open(f'Output/ReadyToSend/my_letter_for_{striped_name}.txt', 'w') as my_new_letter:
            my_new_letter.write(f"{new_letter}")



# with open('Input/Letters/starting_letter.txt') as data:
#     letter = data.read()
#     for name in all_names:
#         stripped_name = name.strip()
#         new_letter = letter.replace(PLACEHOLDER, stripped_name)
#         with open('Output/ReadyToSend/new_letter.txt', mode='w') as my_new_letter:
#             my_new_letter.write(new_letter)
#


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


