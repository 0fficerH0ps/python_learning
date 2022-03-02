# You can create almost any set of numbers you want to using the range()
# function. For example, consider how you might make a list of the first 10
# square numbers (that is, the square of each integer from 1 through 10). In
# Python, two asterisks (**) represent exponents. Here’s how you might put
# the first 10 square numbers into a list:
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)


# a better way to wright it
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
# Focus first on writing code that you understand clearly, which does what you want it to do.
# Then look for more efficient approaches as you review your code.

# Simple Statistics with a List of Numbers
# >>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# >>> min(digits)
# 0
# >>> max(digits)
# 9
# >>> sum(digits)
# 45


# List Comprehensions
# The following example builds the same list of square numbers you saw
# earlier but uses a list comprehension:
squares = [value**2 for value in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
