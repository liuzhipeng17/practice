# coding=utf-8

# log装饰器，分为无参，有参两种
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print "call %s " % func.__name__
        func(*args, **kwargs)

    return wrapper


@log
def index():
    print "function index"


index()
print index.__name__
