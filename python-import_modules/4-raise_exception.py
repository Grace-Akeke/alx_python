def raise_exception():
    value = "Hello, World!"
    if not isinstance(value, int):
        raise TypeError("Expection has been raised")
