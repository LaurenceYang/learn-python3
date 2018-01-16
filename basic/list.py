classmates = ['yang', 'wang', 'han']
print('classmates=', classmates)
print('classmates[0]=', classmates[0])
print('classmates[1]=', classmates[1])
print('classmates[2]=', classmates[2])
print('classmates[-1]=', classmates[-1])  # 用-1做索引，直接获取最后一个元素
classmates.pop()
print("classmates=", classmates)
classmates.append('li')
print("classmates=", classmates)
classmates.insert(1, "ma")
print("classmates=", classmates)
