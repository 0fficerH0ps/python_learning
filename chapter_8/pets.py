# When you call a function, Python must match each argument in the function
# call with a parameter in the function definition. The simplest way to
# do this is based on the order of the arguments provided. Values matched
# up this way are called positional arguments.
# To see how this works, consider a function that displays information
# about pets. The function tells us what kind of animal each pet is and the
# pet’s name, as shown here:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls

# You can call a function as many times as needed. Describing a second, different
# pet requires just one more call to describe_pet():
describe_pet('dog', 'willie')

# Order Matters in Positional Arguments

# You can get unexpected results if you mix up the order of the arguments in
# a function call when using positional arguments:

describe_pet('harry', 'hamster')

# Keyword Arguments

# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion

describe_pet(animal_type='hamster', pet_name='harry')

# Default Values

# When writing a function, you can define a default value for each parameter.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

# Note that the order of the parameters in the function definition had
# to be changed. Because the default value makes it unnecessary to specify a
# type of animal as an argument, the only argument left in the function call
# is the pet’s name. Python still interprets this as a positional argument, so if
# the function is called with just a pet’s name, that argument will match up
# with the first parameter listed in the function’s definition. This is the reason
# the first parameter needs to be pet_name.

# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to continue
# interpreting positional arguments correctly.

# Equivalent Function Calls

# It doesn’t really matter which calling style you use. As long as your function calls produce
# the output you want, just use the style you find easiest to understand.

# Avoiding Argument Errors

# Python is helpful in that it reads the function’s code for us and tells us
# the names of the arguments we need to provide. This is another motivation
# for giving your variables and functions descriptive names. If you do,
# Python’s error messages will be more useful to you and anyone else who
# might use your code.

# If you provide too many arguments, you should get a similar traceback
# that can help you correctly match your function call to the function
# definition.
