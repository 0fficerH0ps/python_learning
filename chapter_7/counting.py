# Introducing while Loops

# The for loop takes a collection of items and executes a block of code once
# for each item in the collection. In contrast, the while loop runs as long as,
# or while, a certain condition is true.

# You can use a while loop to count up through a series of numbers. For
# example, the following while loop counts from 1 to 5:

# current_number = 1
# while current_number <= 5:
#    print(current_number)
#    current_number += 1

# Using continue in a Loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Infinite Loops

x = 1
while x <= 5:
    print(x)
    x += 1

# But if you accidentally omit the line x += 1 (as shown next), the loop
# will run forever:

# This loop runs forever!
# x = 1
# while x <= 5:
 #    print(x)

# Now the value of x will start at 1 but never change. As a result, the conditional test x <= 5 will always evaluate to True and the while loop will run
# forever, printing a series of 1s

