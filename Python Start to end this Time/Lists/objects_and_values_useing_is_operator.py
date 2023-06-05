a = 'banana'
b = 'banana'

print(a is b)  # this will return true or false which means either both
# variables belong to same object, or they belong to a different object

"""
In this example, Python only created one string object, and both a and b refer to it.
But when you create two lists, you get two objects:

 
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

 
False
"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
