# Now we’ll make a separate file called making_pizzas.py in the same
# directory as pizza.py. This file imports the module we just created and then
# makes two calls to make_pizza():

import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When Python reads this file, the line import pizza tells Python to open
# the file pizza.py and copy all the functions from it into this program. You
# don’t actually see code being copied between files because Python copies
# the code behind the scenes just before the program runs. All you need
# to know is that any function defined in pizza.py will now be available in
# making_pizzas.py.

# To call a function from an imported module, enter the name of
# the module you imported, pizza, followed by the name of the function,
# make_pizza(), separated by a dot 7. This code produces the same output
# as the original program that didn’t import a module:

# Making a 16-inch pizza with the following toppings:
# - pepperoni
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese


# Importing Specific Functions
# You can also import a specific function from a module. Here’s the general
# syntax for this approach:

# from module_name import function_name

# You can import as many functions as you want from a module by separating
# each function’s name with a comma:

# from module_name import function_0, function_1, function_2

# The making_pizzas.py example would look like this if we want to import
# just the function we’re going to use:

from pizza_module import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# With this syntax, you don’t need to use the dot notation when you call a
# function. Because we’ve explicitly imported the function make_pizza() in the
# import statement, we can call it by name when we use the function.


# Using as to Give a FUNCTION an Alias

# If the name of a function you’re importing might conflict with an existing
# name in your program or if the function name is long, you can use a
# short, unique alias—an alternate name similar to a nickname for the function.
# You’ll give the function this special nickname when you import the
# function.
# Here we give the function make_pizza() an alias, mp(), by importing
# make_pizza as mp. The as keyword renames a function using the alias you
# provide:

from pizza_module import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# The import statement shown here renames the function make_pizza() to
# mp() in this program. Any time we want to call make_pizza() we can simply
# write mp() instead, and Python will run the code in make_pizza() while avoiding
# any confusion with another make_pizza() function you might have written
# in this program file.

# The general syntax for providing an alias is:

# from module_name import function_name as fn


# Using as to Give a MODULE an Alias

# You can also provide an alias for a module name. Giving a module a short
# alias, like p for pizza, allows you to call the module’s functions more quickly.
# Calling p.make_pizza() is more concise than calling pizza.make_pizza():

import pizza_module as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The module pizza is given the alias p in the import statement, but all of
# the module’s functions retain their original names. Calling the functions by
# writing p.make_pizza() is not only more concise than writing pizza.make_pizza(),
# but also redirects your attention from the module name and allows you
# to focus on the descriptive names of its functions. These function names,
# which clearly tell you what each function does, are more important to the
# readability of your code than using the full module name.

# The general syntax for this approach is:

# import module_name as mn


# Importing All Functions in a Module

# You can tell Python to import every function in a module by using the asterisk
# (*) operator:

from pizza_module import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# However, it’s best not to use this approach when you’re working
# with larger modules that you didn’t write: if the module has a function
# name that matches an existing name in your project, you can get some
# unexpected results. Python may see several functions or variables with the
# same name, and instead of importing all the functions separately, it will
# overwrite the functions.

# I include this section so you’ll
# recognize import statements like the following when you see them in other
# people’s code:

# from module_name import *


# If you specify a default value for a parameter, no spaces should be used
# on either side of the equal sign:

# def function_name(parameter_0, parameter_1='default value')

# The same convention should be used for keyword arguments in function
# calls:

# function_name(value_0, parameter_1='value')

# All import statements should be written at the beginning of a file.
# The only exception is if you use comments at the beginning of your file to
# describe the overall program.
