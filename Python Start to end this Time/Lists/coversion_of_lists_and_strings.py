# converting a string into a list
s = 'abcd'
list_1 = list(s)
print(list_1)

# If you want to break a string
# into words, you can use the split method
s2 = "i am a CS student"

list2 = s2.split()

print(list2)

# using a delimiter(an optional argument)
s3 = 'spam-spam-spam'
delimiter = '-'
list3 = s3.split('-')  # You can also use it this way list3 = s3.split(delimiter)
# it works the same way


print(list3)

# Using the join() method to join/concatenate the strings
rejoin = "-".join(list3)
print("Rejoined list3(Split) through join(): ", rejoin)
