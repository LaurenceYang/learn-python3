import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程的student对象
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student对象
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('yang',), name='Thread_A')
t2 = threading.Thread(target=process_thread, args=('king',), name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()