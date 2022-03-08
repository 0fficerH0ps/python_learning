# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class Users:
    """A model of a user account,"""

    def __init__(self, first_name, last_name, fav_color = None, age = None, height = None):
        """Inatialize basic user info."""
        self.first = first_name
        self.last = last_name
        self.fav_color = fav_color
        self.age = age
        self.height = height

    def describe_user(self):
        """Provide description of user info."""
        full_name = self.first + self.last
        formatted_name = full_name.title()
        print(f"{formatted_name}'s fav color is {self.fav_color}.")
        print(f"They are {self.age} years old and {self.height} tall.")

    def greet_user(self):
        """Greet user with personalised greeting."""
        full_name = self.first + self.last
        formatted_name = full_name.title()
        print(f"Hello {formatted_name}, what can I help you with today?")


sammy = Users('sam', 'smith', age = '5')
sammy.describe_user()
sammy.greet_user()

bobby = Users('bob', 'mayerhoffer', 'yellow', height = '6ft')
bobby.describe_user()
bobby.greet_user()

jacky = Users('jack', 'frost', fav_color = 'blue', age = '16', height = '5ft 8in')
jacky.describe_user()
jacky.greet_user()

# Tested, works 3/8/22