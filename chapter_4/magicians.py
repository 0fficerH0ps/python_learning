# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
# “For every magician in the list of magicians, print the magician’s name.”

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

	print(f"I can't wait to see your next trick, {magician.title()}.\n")
	# Every indented line following the line for magician in magicians is considered
	# inside the loop, and each indented line is executed once for each value in the list.
# outputs:
# 	Alice, that was a great trick!
#	I can't wait to see your next trick, Alice.
#	David, that was a great trick!
#	I can't wait to see your next trick, David.
#	Carolina, that was a great trick!
#	I can't wait to see your next trick, Carolina.

# Doing Something After a for Loop
print("Thank you, everyone. That was a great magic show!")
# The first two calls to print() are repeated once for each magician in the
# list, as you saw earlier. However, because the line is not indented, it’s
# printed only once

# Always indent the line after the for statement in a loop. If you forget, Python will remind you
# The colon at the end of a for statement tells Python to interpret the next
# line as the start of a loop.
