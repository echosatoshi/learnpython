#Fibonacci numbers module fibo.py
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
        print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
    
#test.py
import fibo
fibo.fib(10000)
fibo.fib2(100)
fib = fibo.fib
fib(30)

from fibo import fib, fib2
fib(300)

from fibo import *
fib(300)

#packages
#sound/
#    __init__.py
#    formats/
#        __init__.py
#        wavread.py
#        ...
#    effects/
#        __init__.py
#        echo.py
#        ...
# __init__.py  __all__=['echo', 'surround', 'reverse']
import sound.effects.echo
from sound.effects import echo
from sound.effects.echo import echofilter
