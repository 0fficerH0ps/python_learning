# To make a slice, you specify the index of the first and last elements you
# want to work with. As with the range() function, Python stops one item
# before the second index you specify. To output the first three elements
# in a list, you would request indices 0 through 3, which would return elements
# 0, 1, and 2.
# The following example involves a list of players on a team:

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']

# You can generate any subset of a list. For example, if you want the second,
# third, and fourth items in a list, you would start the slice at index 1 and
# end at index 4:
print(players[1:4]) # ['martina', 'michael', 'florence']

# If you omit the first index in a slice, Python automatically starts your
# slice at the beginning of the list:
print(players[:4]) # ['charles', 'martina', 'michael', 'florence']

# A similar syntax works if you want a slice that includes the end of a list.
# For example, if you want all items from the third item through the last item,
# you can start with index 2 and omit the second index:
print(players[2:]) # ['michael', 'florence', 'eli']

# This syntax allows you to output all of the elements from any point in
# your list to the end regardless of the length of the list. Recall that a negative
# index returns an element a certain distance from the end of a list;
# therefore, you can output any slice from the end of a list. For example, if
# we want to output the last three players on the roster, we can use the slice
# players[-3:]:
print(players[-3:])
# This prints the names of the last three players and would continue to
# work as the list of players changes in size.

# You can include a third value in the brackets indicating a slice. If a third value is
# included, this tells Python how many items to skip between items in the specified
# range.


# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())