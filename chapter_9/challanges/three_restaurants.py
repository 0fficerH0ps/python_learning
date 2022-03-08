# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

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

your_shop = Restaurant('Valintinos', 'Itilian')
your_shop.describe_restaurant()

his_shop = Restaurant("Mama's Boy", 'Taste of Home')
his_shop.describe_restaurant()

her_shop = Restaurant("Tina's Diner", 'Western')
her_shop.describe_restaurant()

# Tested, works 3/7/22