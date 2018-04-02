#!/usr/bin/env python
# coding=utf-8
squares = [1,4,9,16]
sum = 0
for num in squares:
    sum += num
print sum
if 4 in squares :
    print "4 in squares"

if 5 in squares :
    print "5 in squares"
else:
    print "5 not in squares"
string = "hello"
for ch in string :
    print ch

for i in range(10,20):
    print str(i) + " ",
