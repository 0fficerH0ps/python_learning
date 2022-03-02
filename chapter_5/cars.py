cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Equality
# Most conditional tests compare the current value of a variable to a specific
# value of interest. The simplest conditional test checks whether the value of a
# variable is equal to the value of interest:
# >>> car = 'bmw'
# >>> car == 'bmw'
# True

# Testing for equality is case sensitive in Python. For example, two values with
# different capitalization are not considered equal:
# >>> car = 'Audi'
# >>> car == 'audi'
# False

# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True