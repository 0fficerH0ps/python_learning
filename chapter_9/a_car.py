# Let’s write a new class representing a car. Our class will store information
# about the kind of car we’re working with, and it will have a method that
# summarizes this information:

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted deescriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


# Setting a Default Value for an Attribute

# When an instance is created, attributes can be defined without being
# passed in as parameters. These attributes can be defined in the __init__()
# method, where they are assigned a default value.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted deescriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values

# You can change an attribute’s value in three ways: you can change the value
# directly through an instance, set the value through a method, or increment
# the value (add a certain amount to it) through a method. Let’s look at each
# of these approaches.

# Modifying an Attribute’s Value Directly

# The simplest way to modify the value of an attribute is to access the attribute
# directly through an instance.

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method

class Car:
#     --snip--

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


# We can extend the method update_odometer() to do additional work
# every time the odometer reading is modified. Let’s add a little logic to
# make sure no one tries to roll back the odometer reading:

class Car:
#    --snip--
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Now update_odometer() checks that the new reading makes sense before
# modifying the attribute.

# Incrementing an Attribute’s Value Through a Method

# Sometimes you’ll want to increment an attribute’s value by a certain
# amount rather than set an entirely new value. Say we buy a used car and
# put 100 miles on it between the time we buy it and the time we register it.
# Here’s a method that allows us to pass this incremental amount and add
# that value to the odometer reading:

class Car:
#   --snip--
    def update_odometer(self, mileage):
        """snip"""
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# 2015 Subaru Outback
# This car has 23500 miles on it.
# This car has 23600 miles on it.

# You can easily modify this method to reject negative increments so no
# one uses this function to roll back an odometer.

# You can use methods like this to control how users of your program update values
# such as an odometer reading, but anyone with access to the program can set the odometer
# reading to any value by accessing the attribute directly. Effective security takes
# extreme attention to detail in addition to basic checks like those shown here.
