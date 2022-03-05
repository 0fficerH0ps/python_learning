# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

messages = ["Hello there.", "New phone, who dis?", "Your brother...", "Oh, hi Mark."]

def show_messages(message):
    """Print out each message from a list of messages."""
    for message in messages:
        print(message)

messages = ["Hello there.", "New phone, who dis?", "Your brother...", "Oh, hi Mark."]

show_messages(messages)

# Tested, works.