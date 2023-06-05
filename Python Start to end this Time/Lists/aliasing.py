"""
The association of a variable with an object is called a ~~reference~~. In this example,
there are two references to the same object.

An object with more than one reference has more than one name, so we say that the
object is ~~aliased~~.

"""
a = [1, 2, 3]
b = a
print("before modifications a:", a)
print("before modifications b:", b)


b[2] = 22

print("after modifications a:", a)
print("after modifications b:", b)

