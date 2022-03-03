# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.

#opt 1
prompt = ("Enter your age to see the price of your ticket. Enter 'quit' to end the program. ")
age = input(prompt)
age = int(age)

if age <= 3:
    print("Your ticket is free.")
elif age <= 12:
    print("Your ticket costs $10.")
elif age <= 123:
    print("Your ticket is $15.")
elif age > 123:
    print("We can't allow people that old in, its a liability thing, sorry.")
    
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# opt 2
prompt = ("Enter your age to see the price of your ticket. Enter 'quit' to end the program. ")
age = input(prompt)
age = int(age)

while age != 'quit':
    message = input(prompt)
    if age <= 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    elif age <= 123:
        print("Your ticket is $15.")
    elif age > 123:
        print("We can't allow people that old in, its a liability thing, sorry.")
    else:
        print(message)

