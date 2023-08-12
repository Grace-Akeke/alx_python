def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = []
    a, b = 0, 1

    while n > 0:
        fibonacci_numbers.append(a)
        a, b = b, a + b
        n -= 1

    return fibonacci_numbers
      

   
   
      