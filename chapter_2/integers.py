# basic maths
print(2 + 3) # 5
print(3 - 2) # 1
print(2 * 3) # 6
print(3 / 2) # 1.5

# exponents
print(3 ** 2) # 9
print(3 ** 3) # 27
print(10 ** 6) # 1000000

# order of opperations
print(2 + 3*4) # 14
print((2 + 3) * 4) # 20
# The spacing in these examples has no effect on how Python evaluates
# the expressions; it simply helps you more quickly spot the operations that
# have priority when you’re reading through the code.

# floats
print(0.1 + 0.1) # 0.2
print(0.2 + 0.2) # 0.4
print(2 * 0.1) # 0.2
print(2 * 0.2) # 0.4

# be aware that you can sometimes get an arbitrary number of decimal places in your answer:
print(0.2 + 0.1) # 0.30000000000000004
print(3 * 0.1) # 0.30000000000000004
# This happens in all languages and is of little concern.

# integers and floats
print(4/2) # 2.0
print(1+2.0) # 3.0
print(2*3.0) # 6.0
print(3.0**2) # 9.0
# Python defaults to a float in any operation that uses a float, even if the
# output is a whole number.

# underscores in numbers
universe_age = 14_000_000_000
# When you print a number that was defined using underscores, Python prints only the digits:
print(universe_age) # 14000000000
# To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature
# works for integers and floats, but it’s only available in Python 3.6 and later.

# multipul assignment
x, y, z = 0, 0, 0
# x=0, y=0, z=0

#constants
MAX_CONNECTIONS = 5000  # When you want to treat a variable as a constant in your code, make
						# the name of the variable all capital letters.
