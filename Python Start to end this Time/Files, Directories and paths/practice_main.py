with open('my_text.txt') as file:
    contents = file.read()
    print(contents)

with open('my_text.txt', mode='a') as file:
    file.write('ayanu wado laanti aahy')


with open('new_file.txt', mode='w') as new_file:
    new_file.write('Ayyanu shaitaan bhi daadho aaw')

