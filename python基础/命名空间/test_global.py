# -*- coding: utf-8 -*-


x = 0

def change():
    global x
    x = 3

def change2():
    x = 5

print "before change2 x: %d" % x
change2()
print 'after change2 x: %d' % x

print 'before change x: %d' % x
change()
print 'after change x: %d' % x
# before change2 x: 0
# after change2 x: 0
# before change x: 0
# after change x: 3
