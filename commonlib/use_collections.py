from collections import namedtuple

# namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print('p.x = ', p.x)
print('p.y = ', p.y)

from collections import deque
#deque,双向列表
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('f')
print(q)

from collections import defaultdict
#默认dict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict
#有序dict,可以保持key的顺序
d = dict([('a', 1), ('c', 2), ('b', 3)])
print(d)
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od, list(od.keys()))

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1

print(c)