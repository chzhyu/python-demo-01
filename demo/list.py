#!/usr/bin/env python
# coding=utf-8
list = ['lary', 'curly', 'moe']
list.append('shemp')
list.insert(1, 'xxx')
list.extend(['yyy', 'zzz'])
print list
print list.index('curly')

list.remove('curly')
list.pop(1)
print list

list = []
list.append(1)
list.append(2)
print list
list = ['a','b','c','d','e']
print list[1:-1]
list[0:2] = 'z'
print list
