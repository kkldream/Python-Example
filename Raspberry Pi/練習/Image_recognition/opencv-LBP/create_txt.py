from os import listdir
from os.path import isfile, join

file = listdir("pos")
txt = open('pos.txt','w')
for f in file:
    fullpath = join("pos", f)
    if isfile(fullpath):
        str = 'pos/%s 1 0 0 50 50\n'%f
        txt.write(str)
print('pos num : %d'%len(file))

file = listdir("neg")
txt = open('neg.txt','w')
for f in file:
    fullpath = join("neg", f)
    if isfile(fullpath):
        str = 'neg/%s\n'%f
        txt.write(str)
print('neg num : %d'%len(file))