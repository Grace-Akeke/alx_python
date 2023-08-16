def raise_exception():
    value = "Hello, World!"
    if not isinstance(value, int):
        raise TypeError("Expected an integer, but got: {}".format(type(value)))

# Calling the function to raise the exception
raise_exception()
