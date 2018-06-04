__author__ = 'Administrator'
def say_hello(i):
    print(i)
def say_you(j):
    print("hello %s"% j)
say_hello("hello")
say_you("jim")

def say(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return 3
a=say(1)
print(a)