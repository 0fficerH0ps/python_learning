# You can also test to see if two numbers are not equal. For example, the
# following code prints a message if the given answer is not correct:

answer = 17
if answer != 42:
print("That is not the correct answer. Please try again!")

#You can include various mathematical comparisons in your conditional
# statements as well, such as less than, less than or equal to, greater than, and
# greater than or equal to:
# >>> age = 19
# >>> age < 21
# True
# >>> age <= 21
# True
# >>> age > 21
# False
# >>> age >= 21
# False

# You may want to check multiple conditions at the same time. For example,
# sometimes you might need two conditions to be True to take an action. Other
# times you might be satisfied with just one condition being True. The keywords
# and and or can help you in these situations.

# Using and to Check Multiple Conditions
# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 and age_1 >= 21
# False

# >>> age_1 = 22
# >>> age_0 >= 21 and age_1 >= 21
# True

# To improve readability, you can use parentheses around the individual
# tests, but they are not required. If you use parentheses, your test would look
# like this:
# (age_0 >= 21) and (age_1 >= 21)


# Using or to Check Multiple Conditions
# >>> age_0 = 22
# >>> age_1 = 18
# >>> age_0 >= 21 or age_1 >= 21
# True
# >>> age_0 = 18
# >>> age_0 >= 21 or age_1 >= 21
# False

# Checking Whether a Value Is in a List
# >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
# >>> 'mushrooms' in requested_toppings
# True
# >>> 'pepperoni' in requested_toppings
# False
# To find out whether a particular value is already in a list, use the keyword in.

