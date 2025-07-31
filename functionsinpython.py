# some are built in functions like print,len while some are custom functions
def printhello():
    print("Hello,World!!! ")

printhello()

def printname(name):#function with inputs
    print(f"Hello {name},Welcome to Python Tutorial")
printname("Pratik")


def additionofnumbers(*args):#with *args parameter,function can accept multiple arguments and that arguments will be stored in args list
    return sum(args)
print(additionofnumbers(10,20,30))

#lambda functions in python so ..lamba function is a anonymous function with no name...lambda functions is used when we want to do just small work
square=lambda x:x*x
print(square(5))

is_even=lambda x:x%2==0
print(is_even(11))

sum=lambda a,b :a+b
print(sum(a,b))