

'''
From here i start Practicing the dictionary.
'''


# constants = {"pi": 3.14, "e": 2.71, "root 2": 1.41}
# print(constants)
# print(constants["pi"])
# 
# 
# for item in constants:
#     print(f"{item} = {constants[item]}")



results = {'Pass': 3, 'Fail': 0}

results['Moderate'] = 0.5
addition = 0
sum_of_elements = 0
for item in results:
    value_s = results[item]
    addition += 1
    sum_of_elements += value_s
    

print(results)
print(f"total elements: {addition}\nSum of all elements: {sum_of_elements}")
