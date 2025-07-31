try:
    f=open('textfile.txt')
except Exception as e:
    print("Sorry,This file is Not Available",e)

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero")
else:#else block is executed only when error has not occured
    print("Result is", result)
finally:#finaaly block is excuted irrespective of block
    print("Always runs")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

divide(5, 0)  # raises ZeroDivisionError with your message
