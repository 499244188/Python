# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 10:01:10 2017

@author: Z
"""
from collections import namedtuple
Point = namedtuple('Point',['x','y','z'])
p = Point(3,34,2)
for i in p:
    print(i)


    
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('zzz')


from collections import defaultdict
dd = defaultdict(lambda:'XXX')
dd['key'] = 123
dd['key2']

#OrderedDict
from collections import OrderedDict
d = dict([('a',23),('z',21),('x','234')])
od = OrderedDict([('a',23),('z',21),('x','234')])

#Counter
from collections import Counter
c = Counter()
for i in '23432342423423243234234':
    c[i] = c[i]+1
     
     





