# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.

# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class Users:
    """A model of a user account,"""

    def __init__(self, first_name, last_name, fav_color = None, age = None, height = None, login_attempts = 0):
        """Inatialize basic user info."""
        self.first = first_name
        self.last = last_name
        self.fav_color = fav_color
        self.age = age
        self.height = height
        self.login_attempts = login_attempts

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

    def increment_login_attempts(self):
        """Increment amount of times logged in by 1 per attempt."""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        """Reset the user login attempts count."""
        self.login_attempts = 0

sammy = Users('sam', 'smith', age = '5')
sammy.increment_login_attempts()
sammy.increment_login_attempts()
sammy.increment_login_attempts()
sammy.increment_login_attempts()
sammy.increment_login_attempts()
print(f"Login Attempts: {sammy.login_attempts}")

sammy.reset_login_attempts()
print(f"Login Attempts: {sammy.login_attempts}")

# Tested, works 3/8/22