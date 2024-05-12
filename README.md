# Functional Programming and Built-in Modules in Python

This repository contains Python code for the following tasks:

## Task 1: Closures and Fibonacci Sequence

**Description:**
Implement a caching function `caching_fibonacci` that utilizes closures to create and utilize a cache for storing previously calculated Fibonacci numbers.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting from 0 and 1. Mathematically, the nth Fibonacci number can be expressed as:

```
Fn = Fn-1 + Fn-2
```

This task can be solved recursively by calling the function to calculate numbers until the sequence reaches members less than n = 1, where the sequence is defined.

**Requirements:**

- The `caching_fibonacci()` function should return an inner function `fibonacci(n)`.
- `fibonacci(n)` should calculate the nth Fibonacci number.
- If the number is already in the cache, the function should return the value from the cache.
- If the number is not in the cache, the function should calculate it, store it in the cache, and return the result.
- Use recursion to calculate Fibonacci numbers.

**Example Usage:**

```python
# Get the fibonacci function
fib = caching_fibonacci()

# Use the fibonacci function to calculate Fibonacci numbers
print(fib(10))  # Outputs 55
print(fib(15))  # Outputs 610
```

## Task 2: Generator for Income Numbers and Sum

**Description:**
Create functions `generator_numbers` and `sum_profit` to analyze text, identify all valid numbers representing income, and return them as a generator. Additionally, implement `sum_profit` to utilize the `generator_numbers` to calculate the total sum of these numbers and determine the overall profit.

**Requirements:**

- The `generator_numbers(text: str)` function should take a string as an argument and return a generator that iterates over all valid numbers in the text. Valid numbers are considered to be non-erroneous numbers clearly separated by spaces on both sides.
- The `sum_profit(text: str, func: Callable)` function should use the `generator_numbers` generator to compute the total sum of numbers in the input string and accept it as an argument when called.

**Example Usage:**

```python
text = "The employee's total income consists of several parts: 1000.01 as base salary, supplemented by additional earnings of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
```

**Expected Output:**

```
Total income: 1351.46
```

## Task 3
