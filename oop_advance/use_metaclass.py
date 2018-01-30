class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaClass):
    pass

L = MyList()

L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add('END')

print(L)