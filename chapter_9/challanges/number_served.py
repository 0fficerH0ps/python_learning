# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.

# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.

# Part 1
class Restaurant:
    """Basic information about a restaurant."""

    def __init__(self, restaurant_name, restaurant_type, number_served = 0):
        """Initialize name and cuisine attributes."""
        self.name = restaurant_name
        # I decided to change cuisine to the type of restarunt instead.
        self.type = restaurant_type
        self.num_served = number_served

    def describe_restaurant(self):
        """Give description of restaurant."""
        print(f"{self.name} is a {self.type} baised restaurant.")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(f"{self.name} is now open!")

restaurant = Restaurant('Hops Stops', 'Kissaten')
restaurant.num_served = 4
print(restaurant.num_served)

restaurant.num_served = 12
print(restaurant.num_served)


# Part 2

class Restaurants:
    # I changed the class to a plural form to show that each parts work.
    """Basic information about a restaurant."""

    def __init__(self, restaurant_name, restaurant_type, number_served = 0):
        """Initialize name and cuisine attributes."""
        self.name = restaurant_name
        # I decided to change cuisine to the type of restarunt instead.
        self.type = restaurant_type
        self.num_served = number_served

    def describe_restaurant(self):
        """Give description of restaurant."""
        print(f"{self.name} is a {self.type} baised restaurant.")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(f"{self.name} is now open!")

    def set_number_served(self, number_served):
        """Set the amount of customers served."""
        self.num_served = number_served

    def increment_number_served(self):
        """Incrument number served by number of customers."""
        

restaurant = Restaurants('Hops Stops', 'Kissaten')


