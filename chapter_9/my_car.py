# Importing a Single Class

# Now we make a separate file called my_car.py. This file will import the
# Car class and then create an instance from that class:

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Storing Multiple Classes in a Module

# You can store as many classes as you need in a single module, although
# each class in a module should be related somehow. The classes Battery
# and ElectricCar both help represent cars, so let’s add them to the module
# car.py.

# Importing Multiple Classes from a Module

# You can import as many classes as you need into a program file. If we
# want to make a regular car and an electric car in the same file, we need
# to import both classes, Car and ElectricCar

# Using Aliases

# As you saw in Chapter 8, aliases can be quite helpful when using modules
# to organize your projects’ code. You can use aliases when importing classes
# as well.

# As an example, consider a program where you want to make a bunch
# of electric cars. It might get tedious to type (and read) ElectricCar over and
# over again. You can give ElectricCar an alias in the import statement:

# from electric_car import ElectricCar as EC

# Now you can use this alias whenever you want to make an electric car:

# my_tesla = EC('tesla', 'roadster', 2019)
