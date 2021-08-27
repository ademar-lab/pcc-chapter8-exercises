# Store a list of short text messages
messages = ["Hello!", "I'm from Mexico", "I love technology", 
    "I like Harry Potter"]
sent_messages = []

def send_messages(ls_of_messages, sent_messages):
    """Print a list containing different messages"""
    ls_of_messages.reverse()
    while ls_of_messages: 
        sent_message = ls_of_messages.pop()
        print(f"The \"{sent_message}\" message is being sent")
        sent_messages.append(sent_message)

send_messages(messages, sent_messages)
print(f"\nmessages:\n\t{messages}")
print(f"sent messages:\n\t{sent_messages}")