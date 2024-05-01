def fibonacci_search(f, lower_boundary, upper_boundary, tolerance=1e-4, n=100):
    # Create the Fibonacci sequence up to n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])

    # Initial setup
    x1 = lower_boundary + (fib[n - 2] / fib[n]) * (upper_boundary - lower_boundary)
    x2 = lower_boundary + (fib[n - 1] / fib[n]) * (upper_boundary - lower_boundary)
    f1 = f(x1)
    f2 = f(x2)

    # Main loop
    for i in range(1, n - 1):
        if f1 < f2:
            upper_boundary = x2
            x2 = x1
            f2 = f1
            x1 = lower_boundary + (fib[n - i - 2] / fib[n - i]) * (upper_boundary - lower_boundary)
            f1 = f(x1)
        else:
            lower_boundary = x1
            x1 = x2
            f1 = f2
            x2 = lower_boundary + (fib[n - i - 1] / fib[n - i]) * (upper_boundary - lower_boundary)
            f2 = f(x2)


    # Determine the final interval and return the middle point as the minimum
    if f1 < f2:
        minimum = (lower_boundary + x2) / 2
    else:
        minimum = (x1 + upper_boundary) / 2

    return minimum


# Example usage with a simple quadratic function
def example_function(x):
    return x ** 4 / 20 + x / 4 + 1


# Find the minimum of the function on the interval [0, 4]
a = -2
b = 2
n = 100  # Number of iterations

min_point = fibonacci_search(example_function, a, b, n)
print("The minimum point is at x =", min_point)