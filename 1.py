# -*- coding:utf-8 -*-
#numbers
2+2
50-5*6
(50-5*6)/4
8/5
17//3
17%3
5**2

#strings
'"Isn\'," she said.'
s = 'fist line\nsecond line'
print(r'c:\some\name')
print("""\
Usage:thingy[OPTIONS]
    -h
    -H hostname
""")
8*'un' + 'ium'
word = 'python'
word[0] word[5] word[-1] word[-6] word[0:2] word[:2] word[2:] len(word)

#Lists
squres = [1, 4, 9, 16, 25]
squres[0] squres[-1] squres[-3:] squares[:]
squres.append(1) len(squres)
a, b = 0, 1
while b<10:
    print(b)
    print('the value of i is', b)
    print(b, end=',')
    a, b = b, a+b

x = 1
if x<0:
    pass
elif x== 0:
    pass
else:
    pass

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w)>6:
        words.insert(0, w)

for i in range(5):
    pass
range(5, 10)
range(0, 10, 3)
range(-10, -100, -30)
list(range(5))

def fib(n):
    """fibonacci"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)
def fib2(n):
    """return"""
    result = []
    a, b = 0, 1
    while a<n:
        result.append(a)
        a, b = b, a+b
    return result
def parrot(voltage, state='a stiff', action='voom', type='Norwegion'):
    pass
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000, action='voooom')
parrot(action='vooom', voltage=10000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

def cheeseshop(kind, *arguments, **keywords):
    for arg in arguments:
        print(arg)
    print('-'*40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop('Limburger', 'it\'s ver runy, sir', 'it\'s really ver runny, sir', shopkeeper='michael', client='john', sketch='cheese')
def write_mulitiple_items(file, separator, *args):
    file.write(separator.join(args))
def concat(*args, sep='/'):
    return sep.join(args)
concat('earth', 'mars', 'venus')
concat('earth', 'mars', sep='.')

def make_incrementor(n):
    """lambda"""
    return lambda x:x+n
f = make_incrementor(42)
f(0) f(1)
print(make_incrementor.__doc__)




