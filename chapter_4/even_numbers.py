# We can also use the range() function to tell Python to skip numbers in a
# given range. If you pass a third argument to range(), Python uses that value
# as a step size when generating numbers.
# For example, here’s how to list the even numbers between 1 and 10:
even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]

jump_by_5s = list(range(1,30, 5))
print(jump_by_5s) # [1, 6, 11, 16, 21, 26]
# it starts at the first number you give it then jumps by 5 till it hits the number <30

# so if you want jumps of 5 to start at five and end at 30 do this:
count_by_fives = list(range(5,31, 5))
print(count_by_fives) # [5, 10, 15, 20, 25, 30]