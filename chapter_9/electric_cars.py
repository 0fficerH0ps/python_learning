# Importing a Module into a Module

"""A set of classes that can be used to represent electric cars."""
from car import Car

# class Battery:
#     --snip--
# class ElectricCar(Car):
#     --snip--

# The class ElectricCar needs access to its parent class Car, so we import
# Car directly into the module at 4. If we forget this line, Python will raise
# an error when we try to import the electric_car module. We also need to
# update the Car module so it contains only the Car class:

"""A class that can be used to represent a car."""
# class Car:
# --snip--

# Now we can import from each module separately and create whatever
# kind of car we need:

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

