from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# You import multiple classes from a module by separating each class
# with a comma 1. Once you’ve imported the necessary classes, you’re free
# to make as many instances of each class as you need.
# In this example we make a regular Volkswagen Beetle at 3 and an electric
# Tesla Roadster at 6


# Importing an Entire Module

# You can also import an entire module and then access the classes you need
# using dot notation. This approach is simple and results in code that is easy
# to read. Because every call that creates an instance of a class includes the
# module name, you won’t have naming conflicts with any names used in the
# current file.
# Here’s what it looks like to import the entire car module and then create
# a regular car and an electric car:

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# At 26 we import the entire car module. We then access the classes we
# need through the module_name.ClassName syntax. At 28 we again create a
# Volkswagen Beetle, and at 31 we create a Tesla Roadster.

# Importing All Classes from a Module
# You can import every class from a module using the following syntax:
# from module_name import *

# This method is not recommended for two reasons. First, it’s helpful to be
# able to read the import statements at the top of a file and get a clear sense of
# which classes a program uses. With this approach it’s unclear which classes
# you’re using from the module. This approach can also lead to confusion
# with names in the file. If you accidentally import a class with the same name
# as something else in your program file, you can create errors that are hard
# to diagnose. I show this here because even though it’s not a recommended
# approach, you’re likely to see it in other people’s code at some point.
# If you need to import many classes from a module, you’re better off
# importing the entire module and using the module_name.ClassName syntax.
# You won’t see all the classes used at the top of the file, but you’ll see clearly
# where the module is used in the program. You’ll also avoid the potential
# naming conflicts that can arise when you import every class in a module.

