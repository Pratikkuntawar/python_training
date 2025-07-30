# learn about range function that it provides a range of values from 0 to n-1
# basic for loop in python with incrementing by 1
for i in range(0,5):
    print(i)

# basic for loop in python with incrementing by 2
for i in range(0,10,2):
    print(i)

# tried for loop in reverse and got to know that loop starts from 10 and ends in 1 (i.e before zero in reverse loop)
for i in range(10,0,-2):
    print(i)

print("next loop")
# break statemant in python
n=11
for i in range(n):
    if i==n-1:
        print(i)
        print("loop has been ended now")
    else:
        print(i)