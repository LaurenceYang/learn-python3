import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-01-29')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2018-01-29 12:00:00')

today()

print(today.__name__)
