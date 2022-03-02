# A List in a Dictionary

# In the following example, two kinds of information are stored for each
# pizza: a type of crust and a list of toppings. The list of toppings is a value
# associated with the key 'toppings'. To use the items in the list, we give the
# name of the dictionary and the key 'toppings', as we would any value in the
# dictionary. Instead of returning a single value, we get a list of toppings:

# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

# You can nest a list inside a dictionary any time you want more than
# one value to be associated with a single key in a dictionary.