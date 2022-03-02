# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

number = input("How many people are in your dinner group? ")
number = int(number)

if number < 8:
	print("Your table is ready, follow me.")
else:
	print("Allow us a few moments to clear a table for you.")