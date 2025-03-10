a = [1,2,3,4,5,6,7,8,9,10]
# squares = []
# for x in a:
#     squares.append(x**2)
# print(squares)
# squares = [x**2 for x in a]
# print(squares)
# alt = map(lambda x:x ** 2, a)
# print(list(alt))
even_squares = [x**2 for x in a if x % 2 == 0]
# print(even_squares)
alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)
even_squares_dict = {x: x ** 2 for x in a if x % 2 == 0}
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
# print(even_squares_dict)
# print(threes_cubed_set)
alt_dict = dict(map(lambda x: (x, x**2), filter(lambda x: x % 2 == 0, a)))
# print(alt_dict)
alt_set = set(map(lambda x: x ** 3, filter(lambda x: x % 3 == 0, a)))
# print(alt_set)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
# print(flat)
squared = [[x**2 for x in row] for row in matrix]
# print(squared)
a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
# print(f'{b}\n{c}')
matrix = [[1,2,3],[4,5,6],[7,8,9]]
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
# print(filtered)
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size

# result = {}
# for name in order:
#     count = stock.get(name, 0)
#     batches = get_batches(count, 8)
#
#     if batches:
#         result[name] = batches
#
# print(result)
# found = {name: batches for name in order if(batches := get_batches(stock.get(name, 0), 8))}
# has_bug = {name: get_batches(stock.get(name, 0), 4) for name in order if get_batches(stock.get(name, 0), 8)}
# print('Expected:', found)
# print('Found: ', has_bug)
# result = {name: tenth for name, count in stock.items() if(tenth := count // 10) > 0}
# print(result)
# half = [(last := count // 2) for count in stock.values()]
# print(f'Last item of {half} is {last}')
# for count in stock.values():
#     pass
# print(f'Last item of {list(stock.values())} is {count}')
# half = [count // 2 for count in stock.values()]
# print(half)
# print(count)
# found = ((name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8)))
# print(next(found))
# print(next(found))
# def index_words(text):
#     result = []
#     if text:
#         result.append(0)
#     for index, letter in enumerate(text):
#         if letter == ' ':
#             result.append(index + 1)
#     return result
#
import itertools
address = 'Four score and seven years ago...'
# result = index_words(address)
# print(result[:10])
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

# it = index_words_iter(address)
# print(next(it))
# print(next(it))
result = list(index_words_iter(address))
# print(result[:10])
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

# with open('address.txt', 'r') as f:
#     it = index_file(f)
#     results = itertools.islice(it, 0, 10)
#     print(list(results))
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value/total
        result.append(percent)
    return result

visits = [15, 35, 80]
# percentages = normalize(visits)
# print(percentages)
# assert sum(percentages) == 100.0
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# it = read_visits('my_numbers.txt')
# percentages = normalize(it)
# print(percentages)
def normalize_copy(numbers):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
# print(percentages)
assert sum(percentages) == 100
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
# print(percentages)
assert sum(percentages) == 100.0
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
# print(percentages)
assert sum(percentages) == 100.0
# def normalize_defensive(numbers):
#     if iter(numbers) is numbers:
#         raise TypeError('Must supply a container')
#     total = sum(numbers)
#     result = []
#     for value in numbers:
#         percent = 100 * value/total
#         result.append(percent)
#     return result
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

# visits = [15, 35, 80]
# percentages = normalize_defensive(visits)
# assert sum(percentages) == 100.0
# visits = ReadVisits(path)
# percentages = normalize_defensive(visits)
# assert sum(percentages) == 100.0
# visits = [15, 35, 80]
# it = iter(visits)
# normalize_defensive(it)
it = (len(x) for x in open('my_file.txt'))
# print(it)
# print(next(it))
# print(next(it))
roots = ((x, x**0.5) for x in it)
# print(next(roots))
def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

# def animate():
#     for delta in move(4, 5.0):
#         yield delta
#     for delta in pause(3):
#         yield delta
#     for delta in move(2, 3.0):
#         yield delta
def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

def render(delta):
    print(f'Delta: {delta:.1f}')

# def run(func):
#     for delta in func():
#         render(delta)

# run(animate_composed)
import timeit

def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()

# baseline = timeit.timeit(stmt='for _ in slow(): pass', globals=globals(), number=50)
# print(f'Manual nesting {baseline:.2f}s')
# comparison = timeit.timeit(stmt='for _ in fast(): pass', globals=globals(), number=50)
# print(f'Composed nesting {comparison:.2f}s')
#
# reduction = -(comparison- baseline) / baseline
# print(f'{reduction:.1%} less time')
# import math
#
# def wave(amplitude, steps):
#     step_size = 2 * math.pi / steps
#     for step in range(steps):
#         radians = step * step_size
#         fraction = math.sin(radians)
#         output = amplitude * fraction
#         yield output
#
def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')

# def run(it):
#     for output in it:
#         transmit(output)
#
# run(wave(3.0, 8))
# def my_generator():
#     received = yield 1
#     print(f'received = {received}')

# it = iter(my_generator())
# output = next(it)
# print(f'output = {output}')
#
# try:
#     next(it)
# except StopIteration: 
#     pass
# it = iter(my_generator())
# output = it.send(None)
# print(f'output = {output}')
#
# try:
#     it.send('hello!')
# except StopIteration: 
#     pass
# import math
# def wave_modulating(steps):
#     step_size = 2 * math.pi / steps
#     amplitude = yield
#     for step in range(steps):
#         radians = step * step_size
#         fraction = math.sin(radians)
#         output = amplitude * fraction
#         amplitude = yield output
#
# def run_modulating(it):
#     amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
#     for amplitude in amplitudes:
#         output = it.send(amplitude)
#         transmit(output)
#
# run_modulating(wave_modulating(12))
# import math
# def wave_cascading(amplitude_it, steps):
#     step_size = 2 * math.pi / steps
#     for step in range(steps):
#         radians = step * step_size
#         fraction = math.sin(radians)
#         amplitude = next(amplitude_it)
#         output = amplitude * fraction
#         yield output
#
# def complex_wave_cascading(amplitude_it):
#     yield from wave_cascading(amplitude_it, 3)
#     yield from wave_cascading(amplitude_it, 4)
#     yield from wave_cascading(amplitude_it, 5)
#
# def run_cascading():
#     amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
#     it = complex_wave_cascading(iter(amplitudes))
#     for amplitude in amplitudes:
#         output = next(it)
#         transmit(output)
#
# run_cascading()
class MyError(Exception):
    pass
#
# def my_generator():
#     yield 1
#     yield 2 
#     yield 3 
#
# it = my_generator()
# print(next(it))
# print(next(it))
# print(it.throw(MyError('test error')))
def my_generator():
    yield 1

    try:
        yield 2
    except MyError: 
        print('Got MyError')
    else:
        yield 3

    yield 4

# it = my_generator()
# print(next(it))
# print(next(it))
# print(it.throw(MyError('test error')))
# class Reset(Exception):
#     pass
#
# def timer(period):
#     current = period
#     while current:
#         current -= 1
#         try:
#             yield current
#         except Reset: 
#             current = period
#
def check_for_reset():
    # Poll for external event
    ...

def announce(remaining):
    print(f'{remaining} ticks remaining')
#
# def run():
#     it = timer(4)
#     while True:
#         try:
#             if check_for_reset():
#                 current = it.throw(Reset())
#             else:
#                 current = next(it)
#         except StopIteration: 
#             break
#         else:
#             announce(current)
#
# run()
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current

def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()
