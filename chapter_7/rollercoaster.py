# How do you use the int() function in an actual program? Consider a
# program that determines whether people are tall enough to ride a roller
# coaster:

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

# The program can compare height to 48 because height = int(height)
# converts the input value to a numerical representation before the comparison
# is made. If the number entered is greater than or equal to 48, we tell
# the user that they’re tall enough:

# How tall are you, in inches? 71
# You're tall enough to ride!

