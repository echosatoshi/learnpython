bif.__doc__
bif.__name__
bif.__self__
bif.__module__
dir(type)
type(dir)

udf.__doc__
udf.__name__
udf.func_code
udf.func_defaults
udf.func_globals
udf.func_doc
udf.func_name
udf.func_closure

lambdaFunc = lambda x: x*2
lambdaFunc(100)
type(lamdbaFunc)

bim.__doc__
bim.__name__
bim.__self__
type([].append)
dir([].append)

udm.__doc__
udm.__name__
udm.__module__
udm.im_class
udm.im_func
dm.im_self

class C(object):
    def __call__(self, *args):
        print('hello')

c = C()

callable(c)
compile(string, file, type)
eval(obj, globals=glogbals(), locals=locals())
exec obj
input(prompt='')  ====> eval()+raw_input()

#!/usr/bin/env Python

dashes = '\n'+'-'*50
exec_dict = {
'f':"""
for %s in %s:
    print %s
""",
's':"""
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s+1
""",
'n':"""
%s=%d
while %s<%d:
    print %s
    %s=%s+%d
"""
}

def main():
    ltype = raw_input('loop type?(For/While)')
    dtype = raw_input('data type?(Number/seq)')

    if dtype == 'n':
        start = input('starting value?')
        stop = input('ending value(non-inclusive)?')
        step = input('stepping value')
        seq = str(range(start, stop, step))

    else:
        seq = raw_input('enter sequence:')
        var = raw_input('iterative variable name')
        if ltype == 'f':
            exec_str = exec_dict['f'] % (var, seq, var)
        elif ltype == 'w':
            if dtype == 's':
                svar = raw_input('enter sequence name')
                exec_str = exec_dict['s'] % (var, svar, seq, var, svar, svar, var, var, var)
            elif dtype == 'n':
                exec_str = exec_dict['n'] % (var, start, var, stop, var, var, var, step)
    print dashes

if __name__ == '__main__':
    main()


def foo():
    return True
def bar():
    'bar() does not do much'
    return True
foo.__doc__ = 'foo() does not do much'
foo.tester = '''
    if foo():
        print 'passed'
    else:
        print 'failled'
'''

for eachAttr in dir():
    obj = eval(eachAttr)
    if isinstance(obj, type(foo)):
        if hasattr(obj, '__doc__'):
            print '\nFunction "%s" has a doc %s' % (eachAttr, obj.__doc__)
        if hasattr(obj, 'tester'):
            exec obj.tester
    else:
        print '%s' % eachAttr
else:
    print '%s' % eachAttr
