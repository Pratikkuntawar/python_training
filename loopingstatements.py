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

# run a for loop in string and noticed and each character is printed on next line so i will run next loop in such a way that each character will be printed on same line
for char in "hello":
    print(char)

for i in "Pratik":
    print(i,end=" ")
print()
# run a for loop in array
for item in [1,2,3,4,5,6,7,8,9,10]:
    print(item)

# learn about enumerates in python and got to know that it is used in python when we need an index as well as value
fruits=["orange","mango","banana"]
for i in range(len(fruits)):
    print(i,fruits[i])

# and in below code,fruit is used to iterate over values of array
for index,fruit in enumerate(fruits):
    print(index,fruit)

# task ,you will be give array containing values from 10 to 100 diff by 10 in each next value and make use of enumerate function and increment each value by 1
array=[10,20,30,40,50,60,70,80,90,100]
for index,value in enumerate(array):
    array[index]=value+1
    print(index,array[index])

