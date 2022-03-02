requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!") # Hold the anchovies! 

# Numerical Comparisons
# Testing numerical values is pretty straightforward. For example, the following
# code checks whether a person is 18 years old:
# >>> age = 18
# >>> age == 18
# True

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")

# Let’s continue with the pizzeria example. The pizzeria displays a message
# whenever a topping is added to your pizza, as it’s being made. The code for
# this action can be written very efficiently by making a list of toppings the
# customer has requested and using a loop to announce each topping as it’s
# added to the pizza:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# But what if the pizzeria runs out of green peppers? An if statement
# inside the for loop can handle this situation appropriately:

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")


# Using Multiple Lists
# People will ask for just about anything, especially when it comes to pizza
# toppings. What if a customer actually wants french fries on their pizza? You
# can use lists and if statements to make sure your input makes sense before
# you act on it.
# Let’s watch out for unusual topping requests before we build a pizza.
# The following example defines two lists. The first is a list of available toppings
# at the pizzeria, and the second is the list of toppings that the user has
# requested. This time, each item in requested_toppings is checked against the
# list of available toppings before it’s added to the pizza:

available_toppings = ['mushrooms', 'olives', 'green peppers',
						'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

