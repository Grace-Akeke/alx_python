# Assign values to variables 'a' and 'b' in separate lines
a = 1
b = 2

# Import the 'add' function from add_0.py
add = __import__('add_0').add

# Print the result of the addition using string format
print("{} + {} = {}".format(a, b, add(a, b)))