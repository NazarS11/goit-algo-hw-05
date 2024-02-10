import re
from typing import Callable

def generator_numbers(text: str):
    #pattern for searching income values
    pattern = r"\s\d+[\.]{0,1}\d+\s"
    #creating list with finded income values
    incomes = re.findall(pattern, text)
    for income in incomes:
         #generator of income values with stripped spaces
         yield float(income.strip())

def sum_profit(text: str, func: Callable):
    #summarize all income values received from generator
    return sum(func(text))

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.21 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
