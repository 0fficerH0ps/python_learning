prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# This program works well, except that it prints the word 'quit' as if it
# were an actual message. A simple if test fixes this:

    if message != 'quit':
        print(message)

# Now the program makes a quick check before displaying the message
# and only prints the message if it does not match the quit value:

# Setting a flag
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

