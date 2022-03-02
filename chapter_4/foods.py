# Copying a List

# To copy a list, you can make a slice that includes the entire original list
# by omitting the first index and the second index ([:]). This tells Python to
# make a slice that starts at the first item and ends with the last item, producing
# a copy of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

for food in my_foods:
	print(food)

for food in friend_foods:
	print(food)
