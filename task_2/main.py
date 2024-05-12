import re
from typing import Callable, Generator, Text
from functools import reduce
from operator import add

def generator_numbers(text: Text) -> Generator[float, None, None]:
    """
    This function generates a sequence of float numbers found in the input text.
    
    Args:
    text (str): The input text to be processed.
    
    Yields:
    float: A float number found in the input text.
    """
    pattern = r'\b\d+(?:\.\d+)?\b'  # Regular expression pattern to match float numbers
    numbers = re.findall(pattern, text)  # Find all float numbers in the input text
    for number in numbers:
        yield float(number)  # Yield each float number as a generator


def sum_profit(text: Text, func: Callable[[Text], Generator[float, None, None]]) -> float:
    """
    This function calculates the total profit by summing up all float numbers found in the input text.
    
    Args:
    text (str): The input text to be processed.
    func (Callable[[str], Generator[float, None, None]]): A function that generates a sequence of float numbers.
    
    Returns:
    float: The total profit calculated by summing up all float numbers.
    """
    total_income = reduce(add, func(text))  # Calculate the total profit by summing up all float numbers
    return total_income


# Example usage
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")