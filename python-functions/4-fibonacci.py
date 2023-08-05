def fibonacci_sequence(n):
    sequence = []
    if n >= 1: #Add the first number if n >=1
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
        return sequence
        