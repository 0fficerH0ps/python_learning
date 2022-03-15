# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. 

# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. Create an instance of IceCreamStand, 
# and call this method.

class Restaurant:
    """Basic information about a restaurant."""

    def __init__(self, restaurant_name, restaurant_cuisine):
        """Initialize name and cuisine attributes."""
        self.name = restaurant_name
        self.type = restaurant_cuisine

    def describe_restaurant(self):
        """Give description of restaurant."""
        print(f"{self.name} servs {self.type}.")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):
    """
    Represent aspects of a restaurant, 
    Then aspectes specific to an icecream stand.
    """

    def __init__(self, restaurant_name, restaurant_cuisine):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, restaurant_cuisine)
        self.flavor = "vanilla"

    def set_flavors(self, flavors):
        """Store a list of icecream flavors."""
        self.flavor = flavors

    def display_flavors(self):
        """Display a list of flavors."""
        print(self.flavor)

MyStand = IceCreamStand('Hops Stops', 'Ice Cream')

MyStand.set_flavors(['strawberry', 'banana', 'mango'])

MyStand.display_flavors()

# Tested, works 3/15/2022.