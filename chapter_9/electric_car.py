# Parent and child classes, inheritance.

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# The name super comes from a convention of calling the 
# parent class a superclass and the child class a subclass.

# Defining Attributes and Methods for the Child Class

class Car:
    """snip"""
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# Overriding Methods from the Parent Class
# You can override any method from the parent class that doesn’t fit what
# you’re trying to model with the child class. To do this, you define a method
# in the child class with the same name as the method you want to override in
# the parent class. Python will disregard the parent class method and only
# pay attention to the method you define in the child class.
# Say the class Car had a method called fill_gas_tank(). This method is
# meaningless for an all-electric vehicle, so you might want to override this
# method. Here’s one way to do that:

class ElectricCar(Car):
    """snip"""
def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't need a gas tank!")

# Now if someone tries to call fill_gas_tank() with an electric car, Python
# will ignore the method fill_gas_tank() in Car and run this code instead. When
# you use inheritance, you can make your child classes retain what you need
# and override anything you don’t need from the parent class.


# When modeling something from the real world in code, you may find that
# you’re adding more and more detail to a class. You’ll find that you have a
# growing list of attributes and methods and that your files are becoming
# lengthy. In these situations, you might recognize that part of one class can
# be written as a separate class. You can break your large class into smaller
# classes that work together.
# For example, if we continue adding detail to the ElectricCar class, we
# might notice that we’re adding many attributes and methods specific to
# the car’s battery. When we see this happening, we can stop and move those
# attributes and methods to a separate class called Battery. Then we can use a
# Battery instance as an attribute in the ElectricCar class:

class Car:
    """ snip """

class Battery:
    """A simple attempt to model a battery for an electric car."""

def __init__(self, battery_size=75):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size
def describe_battery(self):
    """Print a statement describing the battery size."""
    print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# This looks like a lot of extra work, but now we can describe the battery
# in as much detail as we want without cluttering the ElectricCar class. Let’s
# add another method to Battery that reports the range of the car based on
# the battery size:

class Car:
    """ snip """

class Battery:
    """ snip """

def get_range(self):
    """Print a statement about the range this battery provides."""
    if self.battery_size == 75:
        range = 260
    elif self.battery_size == 100:
        range = 315

print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """ snip """

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
