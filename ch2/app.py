a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print('Middle two:   ', a[3:5])
# print('All but ends: ', a[1:7])
# assert a[:5] == a[0:5]
# assert a[5:] == a[5:len(a)]
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

# print(a[20])
# b = a[3:]
# print('Before:      ', b)
# b[1] = '99'
# print('After:       ', b)
# print('No change:   ', a)
# print('Before:        ', a)
a[2:7] = ['99', '22', '14']
# print('After          ', a)
# print('Before  ',a)
a[2:3] = ['47', '11']
# print('After   ',a)
b = a[:]
assert b == a and b is not a
b = a
# print('Before a', a)
# print('Before b', a)
# a[:] = ["101", "102", "103"]
# assert a is b
# print('After a ', a)
# print('After b ', b)
# x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# odds = x[::2]
# evens = x[1::2]
# print(odds)
# print(evens)
# car_inventory = {
#     'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
#     'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova')
# }
#
# ((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()
# print(f'Best at {loc1} is {best1}, {len(rest1)} others')
# print(f'Best at {loc2} is {best2}, {len(rest2)} others')
def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    ...

# all_csv_rows = list(generate_csv())
# header = all_csv_rows[0]
# rows = all_csv_rows[1:]
# print('CSV Header: ', header)
# print('Row count: ', len(rows))
# it = generate_csv()
# header, *rows = it
# print('CSV Header:', header)
# print('Row count: ', len(rows))
# numbers = [93, 86, 6, 11, 2, 70]
# numbers.sort()
# print(numbers)
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

# tools = [
#     Tool('level', 3.5),
#     Tool('hammer', 1.25),
#     Tool('screwdriver', 0.5),
#     Tool('chisel', 0.25)
# ]
#
# print('Unsorted:', repr(tools))
# tools.sort(key=lambda x: x.name)
# print('\nSorted:  ',tools)
# tools.sort(key=lambda x: x.weight)
# print('By weight:', tools)
power_tools = [
    Tool('drill', 4),
    Tool('Circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4)
]

# power_tools.sort(key=lambda x: (x.weight, x.name))
# power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
# print(power_tools)
# power_tools.sort(key=lambda x: (-x.weight, x.name), reverse=True)
# print(power_tools)
# power_tools.sort(key=lambda x: x.name)
# power_tools.sort(key=lambda x: x.weight, reverse=True)
# print(power_tools)
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy'
}

# print(baby_names)
# print(list(baby_names.keys()))
# print(list(baby_names.values()))
# print(list(baby_names.items()))
# print(baby_names.popitem())
# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} = {value}')
#
# my_func(goose='gosling', kangaroo='joey')
# class MyClass:
#     def __init__(self):
#         self.alligator = 'hatchling'
#         self.elephant = 'calf'
#
# a = MyClass()
# for key, value in a.__dict__.items():
#     print(f'{key} = {value}')
# votes = {
#     'otter': 1281,
#     'polar bear': 587,
#     'fox': 863
# }
#
# def populate_ranks(votes, ranks):
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse=True)
#     for i, name in enumerate(names, 1):
#         ranks[name] = i

# def get_winner(ranks):
#     return next(iter(ranks))
# def get_winner(ranks):
#     for name, rank in ranks.items():
#         if rank == 1:
#             return name
# def get_winner(ranks):
#     if not isinstance(ranks, dict):
#         raise TypeError('must provide a dict instance')
#     return next(iter(ranks))
#
# ranks = {}
# populate_ranks(votes, ranks)
# print(ranks)
# winner = get_winner(ranks)
# print(winner)
# from collections.abc import MutableMapping
from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True) # type: ignore
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

class SortedDict(MutableMapping[str, int]):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)

votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863
}
# sorted_ranks = SortedDict()
# populate_ranks(votes, sorted_ranks)
# print(sorted_ranks.data)
# winner = get_winner(sorted_ranks)
# print(winner)
counters = {
    'pumpernickel': 2,
    'sourdough': 1
}

key = 'wheat'

# if key in counters:
#     count = counters[key]
# else:
#     count = 0
# try:
#     count = counters[key]
# except KeyError: 
#     count = 0
# count = counters.get(key, 0)
# counters[key] = count + 1
# if key not in counters:
#     counters[key] += 1
# counters[key] += 1
# if key in counters:
#     counters[key] += 1
# else:
#     counters[key] = 1
# try:
#     counters[key] += 1
# except KeyError: 
#     counters[key] = 1
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb']
}

key = 'broiche'
who = 'Elmer'

# if key in votes:
#     names = votes[key]
# else:
#     votes[key] = names = []
#
# names.append(who)
# print(votes)
# try:
#     names = votes[key]
# except KeyError: 
#     votes[key] = names = []
#
# names.append(who)
# print(votes)
# names = votes.get(key)
# if names is None:
#     votes[key] = names = []
#
# names.append(who)
# print(votes)
# if(names := votes.get(key)) is None:
#     votes[key] = names = []
#
# names.append(who)
# print(votes)
# names = votes.setdefault(key, [])
# names.append(who)
# print(votes)
# data = {}
# key = 'foo'
# value = []
# data.setdefault(key, value)
# print('Before: ', data)
# value.append('hello')
# print('After: ', data)
# count = counters.setdefault(key, 0)
# counters[key] = count + 1
# print(votes)
visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'}
}

visits.setdefault('France', set()).add('Arles')

if(japan := visits.get('Japan')) is None:
    visits['Japan'] = japan = set()
japan.add('Kyoto')

# print(visits)
# class Visits:
#     def __init__(self):
#         self.data = {}
#
#     def add(self, country, city):
#         city_set = self.data.setdefault(country, set())
#         city_set.add(city)
#
# visits = Visits()
# visits.add('Russia', 'Yekaterinburg')
# visits.add('Tanzania', 'Zanzibar')
# print(visits.data)
from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)

# visits = Visits()
# visits.add('England', 'Bath')
# visits.add('England', 'London')
# print(visits.data)
pictures = {}
path = "/home/seth/Downloads/profile_slate.png"

# if (handle := pictures.get(path)) is None:
#     try:
#         handle = open(path, 'a+b')
#     except OSError: 
#         print(f'Failed to open path {path}')
#         raise
#     else:
#         pictures[path] = handle
#
# handle.seek(0)
# image_data = handle.read()
# print(image_data)
# try:
#     handle = pictures.setdefault(path, open(path, 'a+b'))
# except OSError: 
#     print(f'Failed to open path {path}')
#     raise
# else:
#     handle.seek(0)
#     image_data = handle.read()
#
# print(image_data)
# from collections import defaultdict
#
def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Failed to open path {profile_path}')
        raise
#
# pictures = defaultdict(lambda: open_picture(path))
# handle = pictures[path]
# handle.seek(0)
# image_data = handle.read()
# print(image_data)
class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
print(image_data)
