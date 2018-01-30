class Student(object):
    __slots__ = ('name', 'age')

class GraduateStudent(Student):
    pass

s = Student()

s.name = 'yang'
s.age = 20

s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 100
print('g.score = ', g.score)