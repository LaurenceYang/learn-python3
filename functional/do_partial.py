import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1000000 =', int('1000000', base=2))
print('1010101 =', int2('1010101'))