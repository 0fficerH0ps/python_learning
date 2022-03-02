# Nesting

# Sometimes you’ll want to store multiple dictionaries in a list, or a list of
# items as a value in a dictionary. This is called nesting. You can nest dictionaries
# inside a list, a list of items inside a dictionary, or even a dictionary inside
# another dictionary. Nesting is a powerful feature, as the following examples
# will demonstrate.

	# A List of Dictionaries

	# The alien_0 dictionary contains a variety of information about one alien,
	# but it has no room to store information about a second alien, much less a
	# screen full of aliens. How can you manage a fleet of aliens? One way is to
	# make a list of aliens in which each alien is a dictionary of information about
	# that alien. For example, the following code builds a list of three aliens:

	#	alien_0 = {'color': 'green', 'points': 5}
	#	alien_1 = {'color': 'yellow', 'points': 10}
	#	alien_2 = {'color': 'red', 'points': 15}

	#	aliens = [alien_0, alien_1, alien_2]

	#	for alien in aliens:
	#		print(alien)

# A more realistic example would involve more than three aliens with
# code that automatically generates each alien. In the following example we
# use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


# How might you work with a group of aliens like this? Imagine that one
# aspect of a game has some aliens changing color and moving faster as the
# game progresses. When it’s time to change colors, we can use a for loop and
# an if statement to change the color of aliens. For example, to change the
# first three aliens to yellow, medium-speed aliens worth 10 points each, we
# could do this:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


# You could expand this loop by adding an elif block that turns yellow
# aliens into red, fast-moving ones worth 15 points each. Without showing the
# entire program again, that loop would look like this:

for alien in aliens[0:3]:
	if alien['color'] == 'green':
	alien['color'] = 'yellow'
	alien['speed'] = 'medium'
	alien['points'] = 10
elif alien['color'] == 'yellow':
	alien['color'] = 'red'
	alien['speed'] = 'fast'
	alien['points'] = 15