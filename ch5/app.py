# class SimpleGradebook:
#     def __init__(self):
#         self._grades = {}
#
#     def add_student(self, name):
#         self._grades[name] = []
#
#     def report_grade(self, name, score):
#         self._grades[name].append(score)
#
#     def average_grade(self, name):
#         grades = self._grades[name]
#         return sum(grades) / len(grades)
#
# book = SimpleGradebook()
# book.add_student('Isaac Newton')
# book.report_grade('Isaac Newton', 90)
# book.report_grade('Isaac Newton', 95)
# book.report_grade('Isaac Newton', 85)
#
# print(book.average_grade('Isaac Newton'))
from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
# print(book.average_grade('Albert Einstein'))
class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0

            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count

book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75, 0.05)
book.report_grade('Albert Einstein', 'Math', 65, 0.15)
book.report_grade('Albert Einstein', 'Math', 70, 0.80)
book.report_grade('Albert Einstein', 'Gym', 100, 0.40)
book.report_grade('Albert Einstein', 'Gym', 85, 0.60)
# print(book.average_grade('Albert Einstein'))
grades = []
grades.append((95, 0.45, 'Great job'))
grades.append((85, 0.55, 'Better next time'))
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight, _ in grades)
average_grade = total / total_weight
# print(average_grade)
from collections import namedtuple

Grade = namedtuple('Grade', ('score', 'weight'))
class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self,name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class GradeBook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]

book = GradeBook()
albert = book.get_student('Albert Einstein')
math = albert.get_subject('Math')
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
# print(albert.average_grade())
def log_missing():
    print('Key added')
    return 0

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
# result = defaultdict(log_missing, current)
# print('Before:', dict(result))
# for key, amount in increments:
#     result[key] += amount
# print('After: ', dict(result))
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2

class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)

class InputData:
    def read(self):
        raise NotImplementedError

# class PathInputData(InputData):
#     def __init__(self, path):
#         super().__init__()
#         self.path = path
#
#     def read(self):
#         with open(self.path) as f:
#             return f.read()

class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

# class LineCountWorker(Worker):
#     def map(self):
#         data = self.input_data.read()
#         self.result = data.count('\n')
#
#     def reduce(self, other):
#         self.result += other.result

import os

# def generate_inputs(data_dir):
#     for name in os.listdir(data_dir):
#         yield PathInputData(os.path.join(data_dir, name))
#
# def create_workers(input_list):
    # workers = []
    # for input_data in input_list:
    #     workers.append(LineCountWorker(input_data))
    # return workers

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result
#
# def mapreduce(data_dir):
#     inputs = generate_inputs(data_dir)
#     workers = create_workers(inputs)
#     return execute(workers)
#
import random

def write_test_files(tmpdir):
    os.makedirs(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))

tmpdir = 'test_inputs'
# write_test_files(tmpdir)
#
# result = mapreduce(tmpdir)
# print(f'There are {result} lines')
class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

class LineCountWorker(GenericWorker):
    ...

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

# config = {'data_dir': tmpdir}
# result = mapreduce(LineCountWorker, PathInputData, config)
# print(f'There are {result} lines')
class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesTwo:
    def __init__(self):
        self.value *= 2

class PlusFive:
    def __init__(self):
        self.value += 5

# Example usage
# foo = OneWay(5)
# print('First ordering value is (5 * 2) + 5 =', foo.value)  # Output: 15
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

# bar = AnotherWay(5)
# print('Second ordering value is', bar.value)
# class TimesSeven(MyBaseClass):
#     def __init__(self, value):
#         MyBaseClass.__init__(self, value)
#         self.value *= 7
#
# class PlusNine(MyBaseClass):
#     def __init__(self, value):
#         MyBaseClass.__init__(self, value)
#         self.value += 9
#
# class ThisWay(TimesSeven, PlusNine):
#     def __init__(self, value):
#         TimesSeven.__init__(self, value)
#         PlusNine.__init__(self, value)
#
# foo = ThisWay(5)
# print('Should be (5 * 7) + 9 = 44 but is ', foo.value)
class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)

foo = GoodWay(5)
# print('Should be 7 * (5 + 9) = 98 and is ', foo.value)
mro_str = '\n'.join(repr(cls) for cls in GoodWay.mro())
# print(mro_str)
class ExplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3

class AutomaticTrisect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value /= 3

class ImplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value /= 3

assert ExplicitTrisect(9).value == 3
assert AutomaticTrisect(9).value == 3
assert ImplicitTrisect(9).value == 3

class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)), right=BinaryTree(13, left=BinaryTree(11)))
# print(tree.to_dict())
class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent


    def _traverse(self, key, value):
        if(isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            return value.value
        else:
            return super()._traverse(key, value) # type: ignore

class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
my_tree = NamedSubTree('foobar', root.left.right)
# print(my_tree.to_dict())
import json

class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict()) # type: ignore

# class DataCenterRack(ToDictMixin, JsonMixin):
#     def __init__(self, switch=None, machines=None):
#         self.switch = Switch(**switch) # type: ignore
#         self.machines = [Machine(**kwargs) for str(kwargs) in machines] # type: ignore
#
# class Switch(ToDictMixin, JsonMixin):
#     def __init__(self, ports=None, speed=None):
#         self.ports = ports
#         self.speed = speed
#
# class Machine(ToDictMixin, JsonMixin):
#     def __init__(self, cores=None, ram=None, disk=None):
#         self.cores = cores
#         self.ram = ram
#         self.disk = disk
#
# serialized = """{
#     "switch": {"ports": 5, "speed": 1e9},
#     "machines": [
#         {"cores": 8, "ram": 32e9, "disk": 5e12},
#         {"cores": 4, "ram": 16e9, "disk": 1e12},
#         {"cores": 2, "ram": 4e9, "disk": 500e9}
#     ]
# }"""
#
# deserialized = DataCenterRack.from_json(serialized)
# roundtrip = deserialized.to_json()
# assert json.loads(serialized) == json.loads(roundtrip)

class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

foo = MyObject()
# assert foo.public_field == 5
# assert foo.get_private_field() == 10
# foo.__private_field
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71

class MyParentObject:
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
# assert baz._MyParentObject_._private_field == 71
# print(baz.__dict__)
# class MyStringClass:
#     def __init__(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return str(self.__value)

# foo = MyStringClass(5)
# assert foo.get_value() == '5'
#
# class MyIntegerSubClass(MyStringClass):
#     def get_value(self): # type: ignore
#         return int(self._MyStringClass__value) # type: ignore
#
# foo = MyIntegerSubClass('5')
# assert foo.get_value() == 5
#
# class MyBaseClass:
#     def __init__(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return self.__value

# class MyStringClass(MyBaseClass):
#     def get_value(self):
#         return str(super().get_value())
#
# class MyIntegerSubClass(MyStringClass):
#     def get_value(self):
#         return int(self._MyStringClass__value)
#
# # foo = MyIntegerSubClass(5)
# foo.get_value()
class MyStringClass:
    def __init__(self, value):
        self.__value = value

# class ApiClass:
#     def __init__(self):
#         self._value = 5
#
#     def get(self):
#         return self._value
#
# class Child(ApiClass):
#     def __init__(self):
#         super().__init__()
#         self._value = 'hello' # Conflicts
#
# a = Child()
# print(f'{a.get()} and {a._value} should be different')
class ApiClass:
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'

a = Child()
# print(f'{a.get()} and {a._value} are different')
class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts

foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
# print('Length is', len(foo))
# foo.pop()
# print('After pop:', repr(foo))
# print('Frequency:', foo.frequency())
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'Index {index} is out of range')

tree = IndexableNode(10, left=IndexableNode(5, left=IndexableNode(2), right=IndexableNode(6, right=IndexableNode(7))), right=IndexableNode(15, left=IndexableNode(11)))

# print('LRR is', tree.left.right.right.value)
# print('Index 0 is', tree[0])
# print('Index 1 is', tree[1])
# print('11 in the tree?', 11 in tree)
# print('17 in the tree?', 17 in tree)
# print('Tree is', list(tree))
# print(len(tree))

class SequenceNode(IndexableNode):
    def __len__(self):
        for count, _ in enumerate(self._traverse(), 1):
            pass
        return count

tree = SequenceNode(10, left=SequenceNode(5, left=SequenceNode(2), right=SequenceNode(6, right=SequenceNode(7))), right=SequenceNode(15, left=SequenceNode(11)))
# print('Tree length is', len(tree))
from collections.abc import Sequence

# class BadType(Sequence):
#     pass
#
# foo = BadType()
class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(10, left=BetterNode(5, left=BetterNode(2), right=BetterNode(6, right=BetterNode(7))), right=BetterNode(15, left=BetterNode(11)))
print('Index of 7 is', tree.index(7))
print('Count of 10 is', tree.count(10))
