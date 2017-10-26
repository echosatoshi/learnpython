#os
import os
os.getcwd()
os.chdir('/server/logs')
os.system('mkdir today')
dir(os)
help(os)

#shutill
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

#glob
import glob
glob.glob('*.py')

#sys
import sys
print(sys.argv)
sys.stderr.write('warning')

#re
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fasterst')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'tea for too'.replace('too', 'two')

#math
import math
math.cos(math.pi/4)
math.log(1024, 2)

#random
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()
ramdom.randrange(6)
