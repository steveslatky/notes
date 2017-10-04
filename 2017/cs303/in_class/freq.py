#! /usr/bin/python
import string
import sys

argc = len(sys.argv)
if argc == 1:
    print "usage:  freq.pl file"
    exit()
elif argc == 2:
    filename = sys.argv[1]
    infile = file(filename,'r')


freq = {}
count = 0
for c in string.ascii_lowercase:
    for z in string.ascii_lowercase:
        freq[c][z] = 0

for line in infile:
    for e,c in enumerate(line.lower)():
        c2  =  line[e + 1]
        if c.isalpha():
            freq[c][c2] = freq[c][c2] + 1
            count = count + 1


keys = freq.keys()
keys.sort()
for c in keys:
  print c,float(freq[c])/count

