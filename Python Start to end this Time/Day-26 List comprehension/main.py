with open('file1.txt') as file1:
    file1_data = file1.readlines()
    # print(file1_data)


with open('file2.txt') as file2:
    file2_data = file2.readlines()


common_numbers = [int(nums) for nums in file1_data if nums in file2_data]

print(f"Common numbers in both text files: {common_numbers}")
