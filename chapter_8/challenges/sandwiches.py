# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwich (*toppings):
    """Provide a list of requested toppings."""
    print(toppings)


make_sandwich('ham', 'cheese')
make_sandwich('bacon', 'lettuce', 'tomatoe')
make_sandwich('bacon', 'hashed brown', 'fried egg', 'cheese')

# Tested, works.