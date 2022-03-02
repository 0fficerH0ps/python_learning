name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Sometimes you’ll want to write a prompt that’s longer than one line.
# For example, you might want to tell the user why you’re asking for certain
# input. You can assign your prompt to a variable and pass that variable to the
# input() function. This allows you to build your prompt over several lines,
# then write a clean input() statement.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# When you use the input() function, Python interprets everything the user
# enters as a string.
# When you try to use the input to do a numerical comparison u, Python
# produces an error because it can’t compare a string to an integer
# We can resolve this issue by using the int() function, which tells
# Python to treat the input as a numerical value. The int() function converts
# a string representation of a number to a numerical representation

