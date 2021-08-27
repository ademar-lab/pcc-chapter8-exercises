def make_shirt(size = "L", message = "I love Python"):
    """Create a shirt with a message on it"""
    print(f"The shirt's size is {size.upper()}, and it has the message" 
    f" \"{message}\" printed on it")

make_shirt()
make_shirt("m")
make_shirt("s", "This is a different message")