# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Enter a number, and I'll tell you if it is a multipule of 10. ")
number = int(number)

if number % 10 == 0:
	print(f"\nThe number {number} is a multipule of 10.")
else:
	print(f"\nThe number {number} is not a multipule of 10.")
