# Returning a Simple Value

# Let’s look at a function that takes a first and last name, and returns a neatly
# formatted full name:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# This might seem like a lot of work to get a neatly formatted name when
# we could have just written:

print("Jimi Hendrix")

# But when you consider working with a large program that needs to
# store many first and last names separately, functions like get_formatted_name()
# become very useful. You store first and last names separately and then call
# this function whenever you want to display a full name.

# Making an Argument Optional

# Sometimes it makes sense to make an argument optional so that people
# using the function can choose to provide extra information only if they
# want to. You can use default values to make an argument optional.
# For example, say we want to expand get_formatted_name() to handle
# middle names as well. A first attempt to include middle names might look
# like this:

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# But middle names aren’t always needed, and this function as written
# would not work if you tried to call it with only a first name and a last name.
# To make the middle name optional, we can give the middle_name argument
# an empty default value and ignore the argument unless the user provides a
# value. To make get_formatted_name() work without a middle name, we set the
# default value of middle_name to an empty string and move it to the end of the
# list of parameters:

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# This modified version of our function works for people with just a first
# and last name, and it works for people who have a middle name as well
# Optional values allow functions to handle a wide range of use cases
# while letting function calls remain as simple as possible.
