class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

yang = Student('LaurenceYang', '99')
print('yang.get_name() = ', yang.get_name())
print('yang.get_score() = ', yang.get_score())

yang.set_score(55)
print('yang.get_name() = ', yang.get_name())
print('yang.get_score() = ', yang.get_score())
print('yang.get_grade() = ', yang.get_grade())

print('Do not use yang._Student__name', yang._Student__name)