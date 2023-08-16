def raise_exception():
    value = "Hello, World!"
    if not isinstance(value, int):
        raise TypeError("Expection has been raised")

# Calling the function to raise the exception
raise_exception()
