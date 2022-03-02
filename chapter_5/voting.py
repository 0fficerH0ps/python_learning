# The following code tests whether
# the person can vote:
age = 17
if age >= 18:
	print("You are old enough to vote!")
# You are old enough to vote!
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")


# Many real-world situations involve more than two possible conditions.
# For example, consider an amusement park that charges different rates for
# different age groups:
# • Admission for anyone under age 4 is free.
# • Admission for anyone between the ages of 4 and 18 is $25.
# • Admission for anyone age 18 or older is $40.
# How can we use an if statement to determine a person’s admission rate?
# The following code tests for the age group of a person and then prints an
# admission price message:

age = 100

if age < 4:
	print("Your admission is free.")
elif age < 18:
	print("Your admission is $25.")
else:
	print("Your admission is $40.")

# a simpler way

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}.")

# adding that senior discount
age = 72
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}.")

# Omitting the else Block
# Python does not require an else block at the end of an if-elif chain. Sometimes
# an else block is useful; sometimes it is clearer to use an additional
# elif statement that catches the specific condition of interest:

age = 2
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
print(f"Your admission cost is ${price}.")

# The extra elif block assigns a price of $20 when the person is 65
# or older, which is a bit clearer than the general else block. With this change,
# every block of code must pass a specific test in order to be executed.

# The else block is a catchall statement. It matches any condition that
# wasn’t matched by a specific if or elif test, and that can sometimes include
# invalid or even malicious data. If you have a specific final condition you are
# testing for, consider using a final elif block and omit the else block. As a
# result, you’ll gain extra confidence that your code will run only under the
# correct conditions.

