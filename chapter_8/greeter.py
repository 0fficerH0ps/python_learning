# Defining a Function

# Here’s a simple function named greet_user() that prints a greeting:

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# This example shows the simplest structure of a function. Line 5 
# uses the keyword def to inform Python that you’re defining a function.
# This is the function definition, which tells Python the name of the function 
# and, if applicable, what kind of information the function needs to do its 
# job. The parentheses hold that information.

# Any indented lines that follow def greet_user(): make up the body of
# the function. The text at line 6 is a comment called a docstring, which describes
# what the function does. Docstrings are enclosed in triple quotes, which
# Python looks for when it generates documentation for the functions in your
# programs.

# The line print("Hello!") 7 is the only line of actual code in the body
# of this function, so greet_user() has just one job: print("Hello!").

# When you want to use this function, you call it. A function call tells
# Python to execute the code in the function. To call a function, you write
# the name of the function, followed by any necessary information in parentheses,
# as shown at 9. Because no information is needed here, calling our
# function is as simple as entering greet_user(). As expected, it prints Hello!


# Passing Information to a Function

# Modified slightly, the function greet_user() can not only tell the user Hello!
# but also greet them by name. For the function to do this, you enter username
# in the parentheses of the function’s definition at def greet_user(). By adding
# username here you allow the function to accept any value of username you
# specify. The function now expects you to provide a value for username each
# time you call it. When you call greet_user(), you can pass it a name, such as
# 'jesse', inside the parentheses:

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')

# Entering greet_user('jesse') calls greet_user() and gives the function the
# information it needs to execute the print() call. The function accepts the
# name you passed it and displays the greeting for that name

# The variable username in the definition of greet_user() is an example of a
# parameter, a piece of information the function needs to do its job. The value
# 'jesse' in greet_user('jesse') is an example of an argument. An argument
# is a piece of information that’s passed from a function call to a function.
# When we call the function, we place the value we want the function to work
# with in parentheses. In this case the argument 'jesse' was passed to the
# function greet_user(), and the value was assigned to the parameter username.

# People sometimes speak of arguments and parameters interchangeably. Don’t be surprised
# if you see the variables in a function definition referred to as arguments or the
# variables in a function call referred to as parameters.


# Using a Function with a while Loop

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#        print(f"\nHello, {formatted_name}!")

# But there’s one problem with this while loop: We haven’t defined a quit
# condition. Where do you put a quit condition when you ask for a series of
# inputs? We want the user to be able to quit as easily as possible, so each
# prompt should offer a way to quit. The break statement offers a straightforward
# way to exit the loop at either prompt:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

