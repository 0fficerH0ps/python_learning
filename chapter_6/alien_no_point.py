# Using get() to Access Values

# Using keys in square brackets to retrieve the value you’re interested in
# from a dictionary might cause one potential problem: if the key you ask for
# doesn’t exist, you’ll get an error.

# For dictionaries, specifically, you can use the get() method to
# set a default value that will be returned if the requested key doesn’t exist.
# The get() method requires a key as a first argument. As a second
# optional argument, you can pass the value to be returned if the key doesn’t
# exist

# If the key 'points' exists in the dictionary, you’ll get the corresponding
# value. If it doesn’t, you get the default value. In this case, points doesn’t
# exist, and we get a clean message instead of an error

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) # No point value assigned.

# If you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None. The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value.
# You’ll see more uses for None in Chapter 8.