# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant:
    """Basic information about a restaurant."""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize name and cuisine attributes."""
        self.name = restaurant_name
        # I decided to change cuisine to the type of restarunt instead.
        self.type = restaurant_type

    def describe_restaurant(self):
        """Give description of restaurant."""
        print(f"{self.name} is a {self.type} baised restaurant.")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(f"{self.name} is now open!")

my_caffee = Restaurant('Hops Stops', 'Kissaten')

print(f"My caffee is called {my_caffee.name}.")
print(f"My caffee is similar to a {my_caffee.type}.")
print(f"\t{my_caffee.type} (喫茶店) means 'tea-drinking shop' and it is a Japanese-style tearoom that is also a coffee shop.")

my_caffee.describe_restaurant()
my_caffee.open_restaurant()

# Tested, works 3/7/22