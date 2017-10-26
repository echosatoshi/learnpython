#expression statements print() write() sys.stdout
s = 'Hello, world'
str(s)
repr(s)
str(1/5)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d}{1:3d}{2:4d}'.format(x, x*x, x*x*x))

'12'.zfill(5)
print('{}'.format('knights'))
print('{0}{1}'.format('one','two'))
print('{1}{0}'.format('two', 'one'))
print('{one}{two}'.format(one='a', two='b'))
print('%5.3f' % math.pi)
f = open('file', 'w')
f.write('')
f.close()

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.tell()

with open('file') as f:
    read_data = f.read()
    for line in f:
        print(line, end=' ')
f.closed

import json
json.dumps([1, 'simple', 'list'])
json.dump(x, f)
x = json.load(f)



