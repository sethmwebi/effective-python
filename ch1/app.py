# def to_str(bytes_or_str):
#     if isinstance(bytes_or_str, bytes):
#         value = bytes_or_str.decode('utf-8')
#     else:
#         value = bytes_or_str
#     return value
#
# print(repr(to_str(b'foo')))
# print(repr(to_str('bar')))

# def to_bytes(bytes_or_str):
#     if isinstance(bytes_or_str, str):
#         value = bytes_or_str.encode('utf-8')
#     else:
#         value = bytes_or_str
#     return value
#
# print(repr(to_bytes(b'foo')))
# print(repr(to_bytes('bar')))
pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15)
]

# for i, (item, count) in enumerate(pantry):
#     print('#%d: %-10s = %.2f' % (i, item, count))
# for i, (item, count) in enumerate(pantry):
#     print('#%d: %-10s = %d' % (i +1, item.title(), round(count)))
# for i, (item, count) in enumerate(pantry):
#     before = '#%d: %-10s = %d' % (i+1, item.title(), round(count))
#     after = '#%(loop)d: %(item)-10s = %(count)d' % {'loop': i + 1, 'item': item.title(), 'count': round(count)}
#
#     assert before == after
# for i, (item, count) in enumerate(pantry):
#     old_style = '#%d: %-10s = %d' % (i + 1, item.title(), round(count))
#
#     new_style = '#{}: {:<10s} = {}'.format(i +1, item.title(), round(count))
#
#     assert old_style == new_style
menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel'
}

# formatted = 'First letter is {menu[oyster][0]!r}'.format(menu=menu)
# print(formatted)
# old_template = (
#     'Today\'s soup is %(soup)s, buy one get two %(oyster)s oysters, and our special entree is %(special)s.'
# )
#
# template = ('Today\'s soup is %(soup)s, buy one get two %(oyster)s oysters, and our special entree is %(special)s.' )
#
# old_formatted = template % {
#     'soup': 'lentil',
#     'oyster': 'kumamoto',
#     'special': 'schnitzel'
# }
#
# new_template = (
#     'Today\'s soup is {soup}, buy one get two {oyster} oysters, and our special entree is {special}.'
# )
#
# new_formatted = new_template.format(
#     soup='lentil',
#     oyster='kumamoto',
#     special='schnitzel'
# )
#
# assert old_formatted == new_formatted
# for i, (item, count) in enumerate(pantry):
#     old_style = '#%d: %-10s = %d' % (i + 1, item.title(), round(count))
#     new_style = '#{}: {:<10s} = {}'.format(i + 1, item.title(), round(count))
#     f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'
#     assert old_style == new_style == f_string
# for i, (item, count) in enumerate(pantry):
#     print(f'#{i+1}: {item.title():<10s} = {round(count)}')
# snack_calories = {
#     'chips': 140,
#     'popcorn': 80,
#     'nuts': 190
# }
#
# items = tuple(snack_calories.items())
# print(items)
# favorite_snacks = {
#     'salty': ('pretzels', 100),
#     'sweet': ('cookies', 180),
#     'veggie': ('carrots', 20)
# }
#
# ((type1, (name1, cals1)), (type2, (name2, cals2)), (type3, (name3, cals3))) = favorite_snacks.items()
#
# print(f'Favorite {type1} is {name1} with {cals1} calories')
# print(f'Favorite {type2} is {name2} with {cals2} calories')
# print(f'Favorite {type3} is {name3} with {cals3} calories')
# def bubble_sort(a):
#     for _ in range(len(a)):
#         for i in range(1, len(a)):
#             if a[i] < a[i-1]:
#                 temp = a[i]
#                 a[i] = a[i-1]
#                 a[i-1] = temp
#
# names = ['pretzels', 'carrots', 'arugula', 'bacon']
# bubble_sort(names)
# print(names)
# def bubble_sort(a):
#     for _ in range(len(a)):
#         for i in range(1, len(a)):
#             if a[i] < a[i-1]:
#                 a[i-1], a[i] = a[i], a[i -1]
#
# names = ['pretzels', 'carrots', 'arugula', 'bacon']
# bubble_sort(names)
# print(names)
# snacks = [('bacon', 350),('donut', 240),('muffin', 190)]
# # for i in range(len(snacks)):
# #     item = snacks[i]
# #     name = item[0]
# #     calories = item[1]
# #     print(f'#{i+1}: {name} has {calories} calories')
# for rank, (name, calories) in enumerate(snacks, 1):
#     print(f'#{rank}: {name} has {calories} calories')
# from random import randint
#
# random_bits = 0
# for i in range(32):
#     if randint(0,1):
#         random_bits |= 1 << i
#
# print(bin(random_bits))
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
# for flavor in flavor_list:
#     print(f'{flavor} is delicious')
# for i in range(len(flavor_list)):
#     flavor = flavor_list[i]
#     print(f'{i + 1}: {flavor}')
# it = enumerate(flavor_list)
# print(next(it))
# print(next(it))
# for i, flavor in enumerate(flavor_list):
#     print(f'{i + 1}: {flavor}')
names = ['ivy', 'diana', 'nambi', 'mercy']
counts = [len(n) for n in names]
# print(counts)
longest_name = None
max_count = 0

# for i in range(len(names)):
#     count = counts[i]
#     if count > max_count:
#         longest_name = names[i]
#         max_count = count
#
# print(longest_name)
# for i, name in enumerate(names):
#     count = counts[i]
#     if count > max_count:
#         longest_name = name
#         max_count = count
#
# print(longest_name)
# for name, count in zip(names, counts):
#     if count > max_count:
#         longest_name = name
#         max_count = count
#
# print(longest_name)
names.append('Millicent')
# for name, count in zip(names, counts):
#     print(name)
# import itertools
# for name, count in itertools.zip_longest(names, counts):
#     print(f'{name}: {count}')
# for i in range(3):
#     print('Loop ', i)
# else:
#     print('Else block!')
# for i in range(3):
#     print('Loop', i)
#     if i == 1:
#         break
# else:
#     print('Else block!')
# for x in []:
#     print('Never runs')
# else:
# #     print('For Else block!')
# while False:
#     print('Never runs')
# else:
#     print('While Else block!')
# a = 4
# b = 9
#
# for i in range(2, min(a,b) + 1):
#     print('Testing', i)
#     if a % i == 0 and b % i == 0:
#         print('Not coprime')
#         break
# else:
#     print('Coprime')
# def coprime(a, b):
#     for i in range(2, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             return False
#     return True
#
# print(coprime(4,9))
# print(coprime(3,6))
# def coprime_alternate(a, b):
#     is_coprime = True
#     for i in range(2, min(a,b) + 1):
#         if a % i == 0 and b % i == 0:
#             is_coprime = False
#             break
#     return is_coprime
#
# print(coprime_alternate(4,9))
# print(coprime_alternate(3,6))
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5
}

def make_lemonade(count):
    ...

def out_of_stock():
    ...

# count = fresh_fruit.get('lemon', 0)
# if count:
#     make_lemonade(count)
# else:
#     out_of_stock()
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

def make_cider(count):
    ...

# count = fresh_fruit.get('apple', 0)
# if count >= 4:
#     make_cider(count)
# else:
#     out_of_stock()
if (count := fresh_fruit.get("apple", 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

def slice_bananas(count):
    ...

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    ...

# pieces = 0
# count = fresh_fruit.get("banana", 0)
# if count >= 2:
#     pieces = slice_bananas(count)
#
# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBananas: 
#     out_of_stock()
# count = fresh_fruit.get('banana', 0)
# if count >= 2:
#     pieces = slice_bananas(count)
# else:
#     pieces = 0
#
# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBananas: 
#     out_of_stock()
# pieces = 0
# if(count := fresh_fruit.get("banana", 0)) >= 2:
#     pieces = slice_bananas(count)
#
# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBananas: 
#     out_of_stock()
# if (count := fresh_fruit.get("banana", 0)) >= 2:
#     pieces = slice_bananas(count)
# else:
#     pieces = 0
#
# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBananas: 
#     out_of_stock()
# count = fresh_fruit.get("banana", 0)
# if count >= 2:
#     pieces = slice_bananas(count)
#     to_enjoy = make_smoothies(pieces)
# else:
#     count = fresh_fruit.get("apple", 0)
#     if count >= 4:
#         to_enjoy = make_cider(count)
#     else:
#         count = fresh_fruit.get('lemon', 0)
#         if count:
#             to_enjoy = make_lemonade(count)
#         else:
#             to_enjoy = 'Nothing'
# if (count := fresh_fruit.get('banana', 0)) >= 2:
#     pieces = slice_bananas(count)
#     to_enjoy = make_smoothies(pieces)
# elif (count := fresh_fruit.get('apple', 0)) >= 4:
#     to_enjoy = make_cider(count)
# elif count := fresh_fruit.get('lemon', 0):
#     to_enjoy = make_lemonade(count)
# else:
#     to_enjoy = 'Nothing'
def pick_fruit():
    ...

def make_juice(fruit, count):
    ...
#
# bottles = []
# fresh_fruit = pick_fruit()
# while fresh_fruit:
#     for fruit, count in fresh_fruit.items():
#         batch = make_juice(fruit, count)
#         bottles.extend(batch)
#     fresh_fruit = pick_fruit()
# bottles = []
# while True:
#     fresh_fruit = pick_fruit()
#     if not fresh_fruit:
#         break
#     for fruit, count in fresh_fruit.items():
#         batch = make_juice(fruit, count)
#         bottles.extend(batch)
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
