# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# • Print the message The first three items in the list are:. Then use a slice to
# 	print the first three items from that program’s list.

# • Print the message Three items from the middle of the list are:. Use a slice to
# 	print three items from the middle of the list.

# • Print the message The last three items in the list are:. Use a slice to print the
# 	last three items in the list.


my_foods = ['pizza', 'falafel', 'carrot cake', 'icecream', 'cannoli', 'watermellon', 'ham']
print("The first three items in the list are:")
for food in my_foods[:3]:
	print(food.title())

print("Three items from the middle of the list are:")
for food in my_foods[2:5]:
	print(food.title())

print("The last three items in the list are:")
for food in my_foods[-3:]:
	print(food.title())


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite
# 	pizzas are:, and then use a for loop to print the first list. Print the message
# 	My friend’s favorite pizzas are:, and then use a for loop to print the second
# 	list. Make sure each new pizza is stored in the appropriate list.
my_pizzas = ['cheese', 'peperonie', 'three meet']
friend_pizzas = my_pizzas[:]

my_pizzas.append('hawayian')
friend_pizzas.append('supream')

print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza)

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
