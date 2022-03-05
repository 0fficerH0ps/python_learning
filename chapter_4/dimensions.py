# Lists work well for storing collections of items that can change throughout
# the life of a program. The ability to modify lists is particularly important
# when you’re working with a list of users on a website or a list of characters in
# a game. However, sometimes you’ll want to create a list of items that cannot
# change. Tuples allow you to do just that. Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple.

# Defining a Tuple

dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1])  # 50

# Let’s see what happens if we try to change one of the items in the tuple dimensions:
# 	dimensions[0] = 250
#   output: The code at u tries to change the value of the first dimension, but
#   Python returns a type error. Basically, because we’re trying to alter a tuple,
#   which can’t be done to that type of object, Python tells us we can’t assign a
#   new value to an item in a tuple

# Looping Through All Values in a Tuple
for dimension in dimensions:
	print(dimension)
# output:
# 200
# 50

# Writing over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable
# that represents a tuple. So if we wanted to change our dimensions, we could
# redefine the entire tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

# output:
# Original dimensions:
# 200
# 50
# Modified dimensions:
# 400
# 100

# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout
# the life of a program.
