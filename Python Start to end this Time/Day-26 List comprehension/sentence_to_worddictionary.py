sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# word_list = sentence.split()

# print(word_list)

result = {k: len(k) for k in sentence.split()}
print(result)
