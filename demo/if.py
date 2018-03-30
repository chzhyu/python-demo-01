#!/usr/bin/env python
# coding=utf-8
speed = 100
mood = 'ok'
if speed >= 80:
    print 'License and registration please'
    if mood == 'terrible' or speed >= 100:
        print 'You have rigth to remain slient'
    elif mood == 'bad' or speed >= 90:
        print "I'm going to write a ticket"
        write_ticket()
    else:
        print "Let's try to keep it under 80 ok?"

print 'over'
if speed >= 80: print "you are so busted"
else:print "have a nice day"
