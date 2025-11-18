#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        # Initialize the sequence with the first two numbers
        fibonacci_sequence = [0, 1]
        
        # Generate the rest of the sequence up to the desired length
        for i in range(2, length):
            # The next number is the sum of the previous two
            next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
            # Append the new number to the sequence
            fibonacci_sequence.append(next_number)
        
        # Print the final sequence
        print(fibonacci_sequence)
    pass