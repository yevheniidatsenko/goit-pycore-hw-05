def caching_fibonacci():
    """
    Returns a function that calculates Fibonacci numbers with caching.
    """
    cache = {}

    def fibonacci(n):
        """
        Calculates the nth Fibonacci number using caching.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result

    return fibonacci

# Example usage:
fib = caching_fibonacci()
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610