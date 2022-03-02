# sorting a list permanently with sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']

# reverse order
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

# Sorting a List Temporarily with the sorted() Function
print("Here is the original list:")
print(cars)
# output: 	Here is the original list:
# 			['toyota', 'subaru', 'bmw', 'audi']


print("\nHere is the sorted list:")
print(sorted(cars))
# output: 	Here is the sorted list:
#			['audi', 'bmw', 'subaru', 'toyota']

print("\nHere is the original list again:")
print(cars)
# output: 	Here is the original list again:
# 			['bmw', 'audi', 'toyota', 'subaru']

# The sorted() function can also accept a reverse=True
# argument if you want to display a list in reverse alphabetical order.

print(cars) # ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars) # ['subaru', 'toyota', 'audi', 'bmw']
# Notice that reverse() doesn’t sort backward alphabetically; it simply
# reverses the order of the list

# Finding the Length of a List
# >>> cars = ['bmw', 'audi', 'toyota', 'subaru']
# >>> len(cars)
# 4
