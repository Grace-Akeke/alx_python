# Assign values to variables 'a' and 'b' in separate lines
a = 1
b = 2
result = add(a, b)
if __name__ == "__main__":
# Import the 'add' function from add_0.py
    from add_0 import add

# Print the result of the addition using string format
print("{} + {} = {}".format(a, b, result))