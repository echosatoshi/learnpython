def scope_test():
    def do_local():
        spam = 'local spam'
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spapm'
    do_local()
    print('after local', spam)
    do_nonlocal()
    print('after nonlocal', spam)
    do_global()
    print('after global', spam)

scope_test()
#test spam
#nonlocal spam
#nonlocal spam
#global spam
print('in global scope', spam)

class MyClass:
    """a simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)

class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

s = 'abc'
it = iter(s)
next(it)

class Reverse:
    """iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


