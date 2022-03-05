# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message):
    """Describe t_shirt and message on it."""
    print(f"Your T-shirt size is {size}, your message is: {message}")

make_shirt('Large', 'Pappa no kiss.')
make_shirt(message = 'Pappa no kiss.', size = 'Medium')
