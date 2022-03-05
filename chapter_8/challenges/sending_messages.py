# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


def show_messages(message):
    """Print out each message from a list of messages."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """
    Simulate sending each message, until none are left.
    Move each message to sent_messages after sent.
    """
    while messages:
        current_message = messages.pop()
        print(f"Message: '{current_message}' Status: Sending...")
        sent_messages.append(current_message)
    print(sent_messages)

messages = ["Hello there.", "New phone, who dis?", "Your brother...", "Oh, hi Mark."]
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)

# Tested, works.