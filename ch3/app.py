# def get_stats(numbers):
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return minimum, maximum
#
lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
# minimum, maximum = get_stats(lengths)
# print(f'Min: {minimum}, Max: {maximum}')
def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x/average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ratio(lengths)

# print(f'Longest: {longest:>4.0%}')
# print(f'Shortest: {shortest:>4.0%}')
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count

minimum, maximum, average, median, count = get_stats(lengths)
# print(f'Min: {minimum}, Max: {maximum}')
# print(f'Average: {average}, Median: {median}, Count {count}')
# def careful_divide(a,b):
#     try:
#         return a / b
#     except ZeroDivisionError: 
#         return None

# x,y = 1,0
# result = careful_divide(x,y)
# if result is None:
#     print('Invalid inputs')
# x,y = 5, 0
# result = careful_divide(x,y)
# if not result:
#     print('Invalid inputs')
# def careful_divide(a,b):
#     try:
#         return True, a / b
#     except ZeroDivisionError: 
#         return False, None
#
# success, result = careful_divide(x,y)
# if not success:
#     print('Invalid inputs')
# def careful_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as e: 
#         raise ValueError('Invalid inputs')
# def careful_divide(a: float, b: float) -> float:
#     """
#     Divides a by b.
#     Raises: ValueError: When the inputs cannot be divided.
#     """
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         raise ValueError('Invalid inputs') 
#
# x, y = 5, 2
# try:
#     result = careful_divide(x,y)
# except ValueError: 
#     print('Invalid inputs')
# else:
#     print('Result is %.1f' % result)
# def sort_priority(values, group):
#     def helper(x):
#         if x in group:
#             return (0, x)
#         return (1, x)
#     values.sort(key=helper)
#
# numbers = [8, 3, 1, 2, 5, 4, 9, 7, 6]
# group = {2, 9, 5, 7}
# sort_priority(numbers, group)
# print(numbers)
# def sort_priority2(numbers, group):
#     found = False
#     def helper(x):
#         nonlocal found
#         if x in group:
#             found = True
#             return (0, x)
#         return (1, x)
#     numbers.sort(key=helper)
#     return found
class Sorter:
    def __init__(self, group):
        self.group = group;
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)
numbers = [8, 3, 1, 2, 5, 4, 9, 7, 6]
group = {2, 9, 5, 7}
sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
# print(numbers)
# def log(message, values):
#     if not values:
#         print(message)
#     else:
#         value_str = ', '.join(str(x) for x in values)
#         print(f'{message}: {value_str}')

# log("My numbers are", [1,2])
# log("Hi there", [])
# def log(message, *values): # The only difference
#     if not values:
#         print(message)
#     else:
#         values_str = ', '.join(str(x) for x in values)
#         print(f'{message}: {values_str}')

# log('My numbers are', 1, 2)
# log('Hi there')
favorites = [7, 33, 99]
# log('Favorite colors', *favorites)
def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

# it = my_generator()
# my_func(*it)
# def log(sequence, message, *values):
#     if not values:
#         print(f'{sequence} - {message}')
#     else:
#         values_str = ', '.join(str(x) for x in values)
#         print(f'{sequence} - {message}: {values_str}')

# log(1, 'Favorites', 7, 33)
# log(1, 'Hi there')
# log('Favorite numbers', 7, 33)
def remainder(number, divisor):
    return number % divisor

assert remainder(20,7) == 6
# def print_parameters(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} = {value}')

# print_parameters(alpha=1.5, beta=9, gamma=4)
# def flow_rate(weight_diff, time_diff):
#     return weight_diff / time_diff
#
weight_diff = 0.5
time_diff = 3
# flow = flow_rate(weight_diff, time_diff)
# print(f'{flow:.3} kg per second')
# def flow_rate(weight_diff, time_diff, period):
#     return (weight_diff / time_diff) * period
#
# flow_per_second =flow_rate(weight_diff, time_diff, 1)
# print(flow_per_second)
# def flow_rate(weight_diff, time_diff, period=1):
#     return (weight_diff / time_diff) * period
#
# flow_per_second = flow_rate(weight_diff, time_diff)
# flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
# print(flow_per_second)
# print(flow_per_hour)
# def flow_rate(weight_diff, time_diff, period=1, units_per_kg=float(1)):
#     return ((weight_diff * units_per_kg) / time_diff) * period
#
# pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
# print(pounds_per_hour)
from time import sleep
from datetime import datetime

# def log(message, when=datetime.now()):
#     print(f'{when}: {message}')
#
# log('Hi there!')
# sleep(0.1)
# log('Hello again!')
# def log(message, when=None):
#     """Log a message with a timestamp
#     Args:
#         message: Message to print.
#         when: datetime of when the message occurred.
#             Defaults to the present time.
#     """
#     if when is None:
#         when = datetime.now()
#     print(f'{when}: {message}')
#
# log('Hi there!')
# sleep(0.1)
# log('Hello again!')
# import json
#
# def decode(data, default={}):
#     try:
#         return json.loads(data)
#     except ValueError: 
#         return default
# import json
# def decode(data, default=None):
#     """Load JSON data from a string.
#     Args:
#         data: JSON data to decode
#         default: Value to return if decoding fails.
#             Defaults to an empty dictionary
#     """
#     try:
#         return json.loads(data)
#     except ValueError:
#         if default is None:
#             default = {}
#         return default
#
# foo = decode('bad data')
# foo['stuff'] = 5
# bar = decode('also bad')
# bar['meep'] = 1
# print('Foo:', foo)
# print('Bar:', bar)
# assert foo is not bar
# from typing import Optional
#
# def log_typed(message: str, when: Optional[datetime]=None) -> None:
#     """Log a message with a timestamp
#     Args:
#       message: Message to print.
#       when: datetime of when the message occurred.
#         Defaults to the present time.
#     """
#     if when is None:
#         when = datetime.now()
#     print(f'{when}: {message}')
def safe_division(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError: 
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# result = safe_division(1.0, 10 ** 500, True, False)
# print(result)
# result = safe_division(1.0, 0, ignore_overflow=True)
# print(result)
# result = safe_division(1.0, 10 ** 500, ignore_overflow=True)
# print(result)
# result = safe_division(1.0, 0, ignore_zero_division=True)
# print(result)
# assert safe_division(1.0, 10 ** 500, True, False) == 0
# result = safe_division(1.0, 0, ignore_zero_division=True)
# assert result == float('inf')
try:
    result = safe_division(1.0, 0)
except ZeroDivisionError:
    pass

assert safe_division(number=2, divisor=5) == 0.4
assert safe_division(divisor=5, number=2) == 0.4
assert safe_division(2, divisor=5) == 0.4
def safe_division_c(numerator, denominator, /, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return numerator / denominator
    except OverflowError: 
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


assert safe_division_c(2, 5) == 0.4

def safe_division_e(numerator, denominator, /, ndigits=10, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError: 
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_e(22, 7, ndigits=2)
# print(result)
from functools import wraps
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

# fibonacci(4)
# print(fibonacci)
help(fibonacci)
# import pickle
# print(pickle.dumps(fibonacci))
