# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

numbers = list(range(1, 100_000_001))

x = min(numbers)
print(x)
y = max(numbers)
print(y)
z = sum(numbers)
print(z)

# [Finished in 6.1s] wow... the power of tech!
