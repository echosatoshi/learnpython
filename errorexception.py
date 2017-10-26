#syntax errors
#exceptions
while True:
    try:
        x = int(input('enter a number'))
        break
    except ValueError:
        print('oops')
except (RuntimeError, TypeError, NameError):
    pass

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('{0}'.format(error))
except ValueError:
    print('could not conver a string to an integer')
except:
    print(sys.exc_info()[0])
    raise

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close() 
        
