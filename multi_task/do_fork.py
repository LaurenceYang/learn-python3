import os

print('process %d start...' % os.getpid())

#only works on unix/linux/macos

pid = os.fork()

if pid == 0:
    print('I am the child process(%d) ande my parent is %d' % (os.getpid(), os.getppid()))
else:
    print('I(%d) am the parent process and just create the child process(%d)' % (os.getpid(), pid))