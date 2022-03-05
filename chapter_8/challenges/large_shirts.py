# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size = 'Large', message = 'I love Python'):
    """Describe t_shirt and message on it."""
    print(f"Your T-shirt size is {size}, your message is: {message}")

make_shirt(size = 'Large')
make_shirt(size = 'Medium')
make_shirt(size = 'Small', message = 'Dynamite comes in small packages...')
