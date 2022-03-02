# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru') returns True
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi') retue=rns False

# Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least ten tests. Have at least five tests evaluate to True and
# 	another five tests evaluate to False.

#1
car = 'Mazda'
print("Is car == 'Mazda'? I predict True.")
print(car == 'Mazda')
#2
print("Is car == 'mazda'? I predict False.")
print(car == 'mazda')
#3
print("Is car.title() == 'Mazda'? I predict True.")
print(car.title() == 'Mazda')
#4
print("Is car.lower() == 'Mazda'? I predict False.")
print(car.lower() == 'Mazda')
#5
car = 'Mazda'
print("Is car == 'Mazda'? I predict True.")
print(car == 'Mazda')
#6
car = "ram"
print("Is car == 'Ram'? I predict False.")
print(car == 'Ram')
#7
print("Is car.title() == 'Ram'? I predict True.")
print(car.title() == 'Ram')
#8
print("Is car.lower() == 'Ram'? I predict False.")
print(car.lower() == 'Ram')
#9
print("Is car.title() == 'Ram'? I predict True.")
print(car.title() == 'Ram')
#10
print("Is car.upper() == 'Ram'? I predict False.")
print(car.lower() == 'Ram')

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings
# • Tests using the lower() method

# • Numerical tests involving equality and inequality, greater than and
# 	less than, greater than or equal to, and less than or equal to

# • Tests using the and keyword and the or keyword

# • Test whether an item is in a list
# • Test whether an item is not in a list

ram_terabytes = 6
if ram_terabytes / 2 == 3:
	print("Wow! That's a lot of RAM!")
else:
	print("Would you like to buy more ram?")

ram_terabytes = 5
if ram_terabytes / 2 == 3:
	print("Wow! Thats a lot of space!")
else:
	print("Would you like to buy more ram?")


value = 6
if value == 6:
	print("High roll!")
elif (value == 5) or (value == 4):
	print("Not a bad role.!")
else:
	print("Iced the dice.")

value = 4
if value == 6:
	print("High roll!")
elif (value == 5) or (value == 4):
	print("Not a bad role.!")
else:
	print("Iced the dice.")

value = 1
if value == 6:
	print("High roll!")
elif (value == 5) or (value == 4):
	print("Not a bad role.!")
else:
	print("Iced the dice.")


devs_list = ['adam', 'rick', 'micha', 'moose']
if 'sam' in devs_list:
	print("Welcome aboard!")
else:
	print("Sorry, matee!")

if 'micha' in devs_list:
	print("Welcome aboard!")
else:
	print("Sorry, matee!")


dice_1 = 1
dice_2 = 1

if dice_1 == 1 and dice_2 ==1:
	print("Snake eyes!")
else:
	print("Safe from the snake!")

dice_1 = 2
dice_2 = 1

if dice_1 == 1 and dice_2 ==1:
	print("Snake eyes!")
else:
	print("Safe from the snake!")

