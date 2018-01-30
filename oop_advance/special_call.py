class Student(object):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('yang')
s()