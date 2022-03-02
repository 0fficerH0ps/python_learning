# A Simple Dictionary

# Consider a game featuring aliens that can have different colors and point
# values. This simple dictionary stores information about a particular alien:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) # green
print(alien_0['points']) # 5
# The dictionary alien_0 stores the alien’s color and point value. The last
# two lines access and display that information

# A dictionary in Python is a collection of key-value pairs. Each key is connected
# to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.
# In fact, you can use any object that you can create in Python as a value in a
# dictionary.
# In Python, a dictionary is wrapped in braces, {}, with a series of keyvalue
# pairs inside the braces, as shown in the earlier example:
alien_0 = {'color': 'green', 'points': 5}

# A key-value pair is a set of values associated with each other. When you
# provide a key, Python returns the value associated with that key. Every key
# is connected to its value by a colon, and individual key-value pairs are separated
# by commas. You can store as many key-value pairs as you want in a
# dictionary.
# The simplest dictionary has exactly one key-value pair, as shown in this
# modified version of the alien_0 dictionary:
alien_0 = {'color': 'green'}

# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color']) # green

# Now you can access either the color or the point value of alien_0. If a
# player shoots down this alien, you can look up how many points they should
# earn using code like this:
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs

# Let’s place the alien on the left edge of
# the screen, 25 pixels down from the top. Because screen coordinates usually
# start at the upper-left corner of the screen, we’ll place the alien on the left
# edge of the screen by setting the x-coordinate to 0 and 25 pixels from the
# top by setting its y-coordinate to positive 25, as shown here:
print(alien_0) # {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# The final version of the dictionary contains four key-value pairs. The
# original two specify color and point value, and two more specify the alien’s
# position.

# Starting with an Empty Dictionary

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1) # {'color': 'green', 'points': 5}
# Here we define an empty alien_0 dictionary, and then add color and
# point values to it. The result is the dictionary we’ve been using in previous
# examples

# Typically, you’ll use empty dictionaries when storing user-supplied data
# in a dictionary or when you write code that generates a large number of
# key-value pairs automatically.

# Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.") # The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") # The alien is now yellow.

# For a more interesting example, let’s track the position of an alien that
# can move at different speeds. We’ll store a value representing the alien’s
# current speed and then use it to determine how far to the right the alien
# should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}") # Original x-position: 0
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}") # New x-position: 2



# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0) # {'color': 'green'}

# Be aware that the deleted key-value pair is removed permanently.

