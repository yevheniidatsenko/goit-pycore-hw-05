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

## README.md

### Task 3: Log File Analyzer

**Description:**

This task involves creating a Python script to analyze log files. The script should be able to read a log file provided as a command-line argument and generate statistics based on logging levels such as INFO, ERROR, DEBUG. Additionally, the user can specify a logging level as a second command-line argument to filter and display all entries for that particular level.

**Requirements:**

- The script should accept a log file path as a command-line argument.
- The script should accept an optional command-line argument following the log file path argument. This argument filters and displays all entries for the specified logging level.
- The script should read and parse the log file, counting the number of entries for each logging level (INFO, ERROR, DEBUG, WARNING).
- Implement a function `parse_log_line(line: str) -> dict` to parse log lines.
- Implement a function `load_logs(file_path: str) -> list` to load logs from the file.
- Implement a function `filter_logs_by_level(logs: list, level: str) -> list` to filter logs by level.
- Implement a function `count_logs_by_level(logs: list) -> dict` to count log entries by level.
- Display the results in a table format showing the number of entries for each level. Implement a function `display_log_counts(counts: dict)` for this purpose.
- The script should handle errors such as missing or unreadable files. Use try/except blocks to handle exceptions.

**Example Usage:**

Running the script:

```bash
python [main.py](<http://main.py/>) /path/to/logfile.log
```

Expected output:

```
Logging Level | Count
---------------|---------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1
```

If the user wants to view all entries for a specific logging level, they can run the script with an additional argument, for example:

```bash
python main.py path/to/logfile.log error
```

This will display both general statistics by level and detailed information for all ERROR level entries:

```
Logging Level | Count
---------------|---------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Log details for level 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

### Task 4: Error Handling with Decorators for Console Assistant Bot

**Description:**

Enhance the console assistant bot from the previous task by incorporating error handling using decorators.

**Requirements:**

- All user input errors should be handled using the `input_error` decorator. This decorator should return appropriate messages to the user, such as "Enter user name", "Give me name and phone please", etc.
- The `input_error` decorator should handle exceptions raised within the handler functions, including KeyError, ValueError, and IndexError. When an exception occurs, the decorator should return an appropriate response to the user without terminating the program.

**Example Usage:**

```
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
Enter a command:
```
