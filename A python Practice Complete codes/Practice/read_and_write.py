with open("my_file.text", 'w') as file:
    for i in range(1, 11):
        file.write(f"I am {i} Line\n")
