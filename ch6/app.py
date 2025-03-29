# class OldResistor:
#     def __init__(self, ohms):
#         self._ohms = ohms
#
#     def get_ohms(self):
#         return self._ohms
#
#     def set_ohms(self, ohms):
#         self._ohms = ohms
#
# r0 = OldResistor(50e3)
# print('Before:', r0.get_ohms())
# r0.set_ohms(10e3)
# print('After: ', r0.get_ohms())
# r0.set_ohms(r0.get_ohms() - 4e3)
# assert r0.get_ohms() == 6e3
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

# r1 = Resistor(50e3)
# r1.ohms = 10e3
# r1.ohms += 5e3
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

# r2 = VoltageResistance(1e3)
# print(f'Before: {r2.current:.2f} amps')
# r2.voltage = 10
# print(f'After: {r2.current:.2f} amps')
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms

# r3 = BoundedResistance(1e3)
# r3.ohms = 0
class FixedResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms is immutable")
        self._ohms = ohms

# r4 = FixedResistor(1e3)
# r4.ohms = 2e3
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

# r7 = MysteriousResistor(10)
# r7.current = 0.01
# print(f'Before: {r7.voltage:.2f}')
# r7.ohms
# print(f'After: {r7.voltage:.2f}')
from datetime import datetime, timedelta

class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'

def fill(bucket, amount):
    now = datetime.now()
    if(now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def deduct(bucket, amount):
    now = datetime.now()
    if(now - bucket.reset_time) > bucket.period_delta:
        return False # Bucket hasn't been filled this period
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

# bucket = Bucket(60)
# fill(bucket, 100)
# print(bucket)
# if deduct(bucket, 99):
#     print('Had 99 quota')
# else:
#     print('Not enough for 99 quota')
# print(bucket)
# if deduct(bucket, 3):
#     print('Had 3 quota')
# else:
#     print('Not enough for 3 quota')
# print(bucket)
class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (f'NewBucket(max_quota={self.max_quota}) quota_consumed={self.quota_consumed}')

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # Quota being reset for a new period
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # Quota being filled for the new period
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # Quota being consumed during the period
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

bucket = NewBucket(60)
# print('Initial', bucket)
# fill(bucket, 100)
# print('Filled', bucket)
#
# if deduct(bucket, 99):
#     print('Had 99 quota')
# else:
#     print('Not enough for 99 quota')
#
# print('Now', bucket)
#
# if deduct(bucket, 3):
#     print('Had 3 quota')
# else:
#     print('Not enough for 3 quota')
#
# print('Still', bucket)
# class Homework:
#     def __init__(self):
#         self._grade = 0
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, value):
#         if not (0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#         self._grade = value
#
# galileo = Homework()
# galileo.grade = 95
#
# class Exam:
#     def __init__(self):
#         self._writing_grade = 0
#         self._math_grade = 0
#
#     @staticmethod
#     def _check_grade(value):
#         if not(0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#
#     @property
#     def writing_grade(self):
#         return self._writing_grade
#
#     @writing_grade.setter
#     def writing_grade(self, value):
#         self._check_grade(value)
#         self._writing_grade = value
#
#     @property
#     def math_grade(self):
#         return self._math_grade
#
#     @math_grade.setter
#     def math_grade(self, value):
#         self._check_grade(value)
#         self._math_grade = value
# class Grade:
#     def __get__(self, instance, instance_type):
#         ...
#
#     def __set__(self, instance, value):
#         ...
# class Grade:
#     def __init__(self):
#         self._value = 0
#
#     def __get__(self, instance, instance_type):
#         return self._value
#
#     def __set__(self, instance, value):
#         if not (0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#         self._value = value
#
# class Exam:
#     # Class attributes
#     math_grade = Grade()
#     writing_grade = Grade()
#     science_grade = Grade()
#
# first_exam = Exam()
# first_exam.writing_grade = 82
# first_exam.science_grade = 99
# # print("Writing", first_exam.writing_grade)
# # print("Science", first_exam.science_grade)
# second_exam = Exam()
# second_exam.writing_grade = 75
# print(f'Second {second_exam.writing_grade} is right')
# print(f'First {first_exam.writing_grade} is wrong; should be 82')
# class Grade:
#     def __init__(self):
#         self._values = {}
#
#     def __get__(self, instance, instance_type):
#         if instance is None:
#             return self
#         return self._values.get(instance, 0)
#
#     def __set__(self, instance, value):
#         if not(0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#         self._values[instance] = value
from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
             return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
# print(f'First {first_exam.writing_grade} is right.')
# print(f'Second {second_exam.writing_grade} is right.')
class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'Value for {name}'
        setattr(self, name, value)
        return value

data = LazyRecord()
# print('Before:', data.__dict__)
# print('foo:   ', data.foo)
# print('After: ', data.__dict__)
class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* Called __getattr__({name!r}) populating instance dictionary')
        result = super().__getattr__(name)
        print(f'* Returning {result!r}')
        return result

data = LoggingLazyRecord()
# print('exists:     ', data.exists)
# print('First foo:  ', data.foo)
# print('Second foo: ', data.foo)
class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* Found {name!r}, returning {value!r}')
            return value
        except AttributeError: 
            value = f'Value for {name}'
            print(f'* Setting {name!r} to {value!r}')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
# print('exists:    ', data.exists)
# print('First foo: ', data.foo)
# print('Second foo:', data.foo)
class MissingPropertyRecord:
    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError(f'{name} is missing')

data = MissingPropertyRecord()
# data.bad_name
data = LoggingLazyRecord() # Implements __getattr__
# print('Before:          ', data.__dict__)
# print('Has first foo:   ', hasattr(data, 'foo'))
# print('After:           ', data.__dict__)
# print('Has second foo:  ', hasattr(data, 'foo'))
data = ValidatingRecord()
# print('Has first foo:    ', hasattr(data, 'foo'))
# print('Has second foo:   ', hasattr(data, 'foo'))
class SavingRecord:
    def __setattr__(self, name, value):
        # Save some data for the record
        ...
        super().__setattr__(name, value)

class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name, value):
        print(f'* Called __setattr__({name!r}, {value!r})')
        super().__setattr__(name, value)

# data = LoggingSavingRecord()
# print('Before:   ', data.__dict__)
# data.foo = 5
# print('After:    ', data.__dict__)
# data.foo = 7
# print('Finally:  ', data.__dict__)
class BrokenDictionaryRecord:
    def __init__(self, data):
        self.data = {}

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        return self._data[name]

data = BrokenDictionaryRecord({'foo': 3})
# data.foo
class DictionaryRecord:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        print(f'* Called __getattribute__({name!r})')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]

data = DictionaryRecord({'foo': 3})
""" print('foo:  ', data.foo) """
# class Meta(type):
#     def __new__(meta, name, bases, class_dict):
#         print(f'* Running {meta}.__new__ for {name}')
#         print('Bases:', bases)
#         print(class_dict)
#         return type.__new__(meta, name, bases, class_dict)
#
# class MyClass(metaclass=Meta):
#     stuff = 123
#
#     def foo(self):
#         pass
#
# class MySubclass(MyClass):
#     other = 567
#
#     def bar(self):
#         pass
# class ValidatePolygon(type):
#     def __new__(meta, name, bases, class_dict):
#         # Only validate subclasses of the Polygon class
#         if bases:
#             if class_dict['sides'] < 3:
#                 raise ValueError('Polygons need 3+ sides')
#             return type.__new__(meta, name, bases, class_dict)
#
# class Polygon(metaclass=ValidatePolygon):
#     sides = None # Must be specified by subclasses
#
#     @classmethod
#     def interior_angles(cls):
#         return (cls.sides - 2) * 180 # type: ignore
#
# class Triangle(Polygon):
#     sides = 3
#
# class Rectangle(Polygon):
#     sides = 4
#
# class Nonagon(Polygon):
#     sides = 9
#
# assert Triangle.interior_angles() == 180
# assert Rectangle.interior_angles() == 360
# assert Nonagon.interior_angles() == 1260
 
# print('Before class')
#
# class Line(Polygon):
#     print('Before sides')
#     sides = 2
#     print('After sides')
#
# print('After class')
# class ValidatePolygon(type):
#     def __new__(meta, name, bases, class_dict):
#         # Only validate subclasses of the Polygon class
#         if bases:
#             if class_dict['sides'] < 3:
#                 raise ValueError('Polygon needs 3+ sides')
#         return type.__new__(meta, name, bases, class_dict)
#
# class Polygon(metaclass=ValidatePolygon):
#     sides = 0 # Must be specified by subclasses
#
#     @classmethod
#     def interior_angles(cls):
#         return (cls.sides - 2) * 180
#
# class Triangle(Polygon):
#     sides = 3
#
# class Rectangle(Polygon):
#     sides = 4
#
# class Nonagon(Polygon):
#     sides = 9
#
# assert Triangle.interior_angles() == 180
# assert Rectangle.interior_angles() == 360
# assert Nonagon.interior_angles() == 1260

# print("Before class")
#
# class Line(Polygon):
#     print('Before sides')
#     sides = 2
#     print("After sides")
#
# print("After class")
class BetterPolygon:
    sides = 0

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('Polygons need 3+ sides')

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180

class Hexagon(BetterPolygon):
    sides = 6

assert Hexagon.interior_angles() == 720

# print("Before class")
#
# class Point(BetterPolygon):
#     sides = 1
#
# print('After class')
# class ValidateFilled(type):
#     def __new__(meta, name, bases, class_dict):
#         # only validate subclasses of the Filled class
#         if bases:
#             if class_dict['color'] not in ('red', 'green'):
#                 raise ValueError('Fill color must be supported')
#         return type.__new__(meta, name, bases, class_dict)
#
# class Filled(metaclass=ValidateFilled):
#     color = None
#
# class RedPentagon(Filled, Polygon):
#     color = 'red'
#     sides = 5
# class ValidatePolygon(type):
#     def __new__(meta, name, bases, class_dict):
#         # Only validate non-root classes
#         if not class_dict['sides'] < 3:
#             raise ValueError('Polygons need 3+ sides')
#         return type.__new__(meta, name, bases, class_dict)
#
# class Polygon(metaclass=ValidatePolygon):
#     is_root = True
#     sides = 0 # Must be specified by subclasses
#
# class ValidateFilledPolygon(ValidatePolygon):
#     def __new__(meta, name, bases, class_dict):
#         # Only validate non-root classes
#         if not class_dict.get('is_root'):
#             if class_dict['color'] not in ('red', 'green'):
#                 raise ValueError('Fill color must be supported')
#         return super().__new__(meta, name, bases, class_dict)
#
# class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
#     is_root = True
#     color = None
#
# class GreenPentagon(FilledPolygon):
#     color = 'green'
#     sides = 5
#
# # greenie = GreenPentagon()
# # assert isinstance(greenie, Polygon)
# class OrangePentagon(FilledPolygon):
#     color = 'orange'
#     sides = 5
#
# class RedLine(FilledPolygon):
#     color = 'red'
#     sides = 2
#
# class Filled:
#     color = None
#
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         if cls.color not in ('red', 'green', 'blue'):
#             raise ValueError('Fills need a valid color')
#
# class RedTriangle(Filled, Polygon):
#     color = 'red'
#     sides = 3
#
# rudy = RedTriangle()
# assert isinstance(rudy, Filled)
# assert isinstance(rudy, Polygon)
#
# print('Before class')
# class BlueLine(Filled, Polygon):
#     color = 'blue'
#     sides = 2
#
# print('After class')
#
# print('Before class')
#
# class BeigeSquare(Filled, Polygon):
#     color = 'beige'
#     sides = 4
#
# print('After class')
# class Top:
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         print(f'Top for {cls}')
#
# class Left(Top):
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         print(f'Left for {cls}')
#
# class Right(Top):
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         print(f'Right for {cls}')
#
# class Bottom(Left, Right):
#     def __init_subclass__(cls):
#         super().__init_subclass__()
#         print(f'Bottom for {cls}')
import json

class Serializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

# point = Point2D(5,3)
# print('Object:    ', point)
# print('Serialized:', point.serialize())
class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class BetterPoint2D(Deserializable):
    ...

# before = BetterPoint2D(5,3)
# print('Before:        ', before)
# data = before.serialize()
# print('Serialized:    ', data)
# after = BetterPoint2D.deserialize(data)
# print('After:         ', after)
class BetterSerializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'class': self.__class__.__name__, 'args': self.args})

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args_str = ', '.join(str(x) for x in self.args)
        return f'{name}({args_str})'

registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

# class EvenBetterPoint2D(BetterSerializable):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.x = x
#         self.y = y
#
# register_class(EvenBetterPoint2D)
#
# before = EvenBetterPoint2D(5,3)
# print('Before:    ', before)
# data = before.serialize()
# print('Serialized:', data)
# after = deserialize(data)
# print('After:     ', after)
# class Point3D(BetterSerializable):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)
#         self.x = x
#         self.y = y
#         self.z = z
#
# point = Point3D(5, 9, -4)
# data = point.serialize()
# deserialize(data)
# class Meta(type):
#     def __new__(meta, name, bases, class_dict):
#         cls = type.__new__(meta, name, bases, class_dict)
#         register_class(cls)
#         return cls
#
# class RegisteredSerializable(BetterSerializable, metaclass=Meta):
#     pass
#
# class vector3D(RegisteredSerializable):
#     def __init__(self, x, y, z):
#         super().__init__(x,y,z)
#         self.x, self.y, self.z = x, y, z

# before = vector3D(10, -7, 3)
# print('Before:    ', before)
# data = before.serialize()
# print('Serialized:', data)
# print('After:     ', deserialize(data))
class BetterRegisteredSerializable(BetterSerializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)

class Vector1D(BetterRegisteredSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude

# before = Vector1D(6)
# print('Before:   ', before)
# data = before.serialize()
# print('Serialized:', data)
# print('After:     ', deserialize(data))
# class Field:
#     def __init__(self, name):
#         self.name = name
#         self.internal_name = '_' + self.name
#
#     def __get__(self, instance, instance_type):
#         if instance is None:
#             return self
#         return getattr(instance, self.internal_name, '')
#
#     def __set__(self, instance, value):
#         setattr(instance, self.internal_name, value)
#
# class Customer:
#     # Class attributes
#     first_name = Field('first_name')
#     last_name = Field('last_name')
#     prefix = Field('prefix')
#     suffix = Field('suffix')

# cust = Customer()
# print(f'Before: {cust.first_name!r} {cust.__dict__}')
# cust.first_name = 'Euclid'
# print(f'After:   {cust.first_name!r} {cust.__dict__}')
# class Field:
#     def __init__(self):
#         # These will be assigned by the metaclass.
#         self.insane = None
#         self.internal_name = None
#
#     def __get__(self, instance, instance_type):
#         if instance is None:
#             return self
#         return getattr(instance, self.internal_name, '') # type: ignore
#
#     def __set__(self, instance, value):
#         setattr(instance, self.internal_name, value) # type: ignore
# class Meta(type):
#     def __new__(meta, name, bases, class_dict):
#         for key, value in class_dict.items():
#             if isinstance(value, Field):
#                 value.name = key
#                 value.internal_name = '_' + key
#         cls = type.__new__(meta, name, bases, class_dict)
#         return cls
#
# class DatabaseRow(metaclass=Meta):
#     pass
#
#
# class BetterCustomer(DatabaseRow):
#     first_name = Field()
#     last_name = Field()
#     prefix = Field()
#     suffix = Field()
#
# # cust = BetterCustomer()
# # print(f'Before: {cust.first_name!r} {cust.__dict__}')
# # cust.first_name = 'Euler'
# # print(f'After:  {cust.first_name!r} {cust.__dict__}')
# class BrokenCustomer:
#     first_name = Field()
#     last_name = Field()
#     prefix = Field()
#     suffix = Field()
#
# cust = BrokenCustomer()
# cust.first_name = 'Mersenne'
class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __set_name__(self, owner, name):
        # Called on class creation for each descriptor
        self.name = name
        self.internal_name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, '') # type: ignore

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value) # type: ignore

class FixedCustomer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

# cust = FixedCustomer()
# print(f'Before: {cust.first_name!r} {cust.__dict__}')
# cust.first_name = 'Mersenne'
# print(f'After:  {cust.first_name!r} {cust.__dict__}')
from functools import wraps

def trace_func(func):
    if hasattr(func, 'tracing'):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')

    wrapper.tracing = True
    return wrapper

class TraceDict(dict):
    @trace_func
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @trace_func
    def __setitem__(self, *args, **kwargs):
        return super().__setitem__(*args, **kwargs)

    @trace_func
    def __getitem__(self, *args, **kwargs):
        return super().__getitem__(*args, **kwargs)

# trace_dict = TraceDict([('hi', 1)])
# trace_dict['there'] = 2
# trace_dict['hi']
# try:
#     trace_dict['does not exist']
# except KeyError: 
#     pass
import types

trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType
)

class TraceMeta(type):
    def __new__(meta, name, bases, class_dict):
        klass = super().__new__(meta, name, bases, class_dict)

        for key in dir(klass):
            value = getattr(klass, key)
            if isinstance(value, trace_types):
                wrapped = trace_func(value)
                setattr(klass, key, wrapped)

        return klass

# class TraceDict(dict, metaclass=TraceMeta):
#     pass
#
# trace_dict = TraceDict([('hi', 1)])
# trace_dict['there'] = 2
# trace_dict['hi']
# try:
#     trace_dict['does not exist']
# except KeyError: 
#     pass
class OtherMeta(TraceMeta):
    pass

class SimpleDict(dict, metaclass=OtherMeta):
    pass

class TraceDict(SimpleDict, metaclass=TraceMeta):
    pass

# trace_dict = TraceDict([('hi', 1)])
# trace_dict['there'] = 2
# trace_dict['hi']
# try:
#     trace_dict['does not exist']
# except KeyError: 
#     pass
def my_class_decorator(klass):
    klass.extra_param = 'hello'
    return klass

@my_class_decorator
class MyClass:
    pass

# print(MyClass)
# print(MyClass.extra_param)
def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass

# @trace
# class TraceDict(dict):
#     pass
#
# trace_dict = TraceDict([('hi', 1)])
# trace_dict['there'] = 2
# trace_dict['hi']
# try:
#     trace_dict['does not exist']
# except KeyError: 
#     pass
class OtherMeta(type):
    pass

@trace
class TraceDict(dict, metaclass=OtherMeta):
    pass

trace_dict = TraceDict([('hi', 1)])
trace_dict['there'] = 2
trace_dict['hi']
try:
    trace_dict['does not exist']
except KeyError: 
    pass
