# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['pastrami', 'ham & cheese', 'pastrami', 'meatball sub', 'pastrami', 'hook & ladder', 'cold cut']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Currently makeing: {sandwich.title()}")
    if sandwich == 'pastrami':
        print("Sorry, we are out of pastrami.")
    else:
        finished_sandwiches.append(sandwich)


print(f"\nThe following orders have been completed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# Okay... now I'm really hungry...