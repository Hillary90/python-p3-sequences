def fibonacci(length):
    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = fibonacci(length)
        print(fib_sequence)
