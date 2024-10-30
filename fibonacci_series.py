def fibonacci(n):
    # Initialize first two terms
    fib_series = [0, 1]
    
    # Generate Fibonacci sequence
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Take input from the user for the number of terms
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# Call the function and display the Fibonacci series
print("Fibonacci series up to", num_terms, "terms:")
print(fibonacci(num_terms))