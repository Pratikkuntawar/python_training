def my_decorator(func):
    def wrapper():
        print("Transaction has been started")
        func()
        print("Transaction has been executed....")
    return wrapper

def hello():
    print("Trnsaction is being executed")

hello1=my_decorator(hello)
hello1()

print("************************************************************************************")

def decorator(func):
    def wrapper(a,b):
        print("before function")
        result=func(a,b)
        print("function has been executed")
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b
print(add(2,3))