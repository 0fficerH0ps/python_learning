# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.



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

def show_sent_messages(sent_messages):
    """Show the messages that were sent."""
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

messages = ["Hello there.", "New phone, who dis?", "Your brother...", "Oh, hi Mark."]
sent_messages = []

send_messages(messages[:], sent_messages)
print(messages)

# Tested, works.