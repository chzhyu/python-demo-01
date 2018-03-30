#!/usr/bin/env python
# coding=utf-8
def sum(a,b):
    c = a + b
    print c
sum(1,2)
s = '  a A    '
print (s.lower())
print (s.upper())
print s.strip()
print s.isalpha()
print s.isdigit()
print s.isspace()
print '--------------------'

s = 'abcde'
print s.startswith('a')
print s.endswith('e')
print s.find('d')
print s.find('z')
print s.replace('c','d')
print '-----------------------'

s = 'abc,dd,fdsa,fda'
print s.split(',')
print '--'.join(['abc','fa','fsad'])
