# Learn about list as list are similaer to array and we can store values of diff types in a same list
# list in mutable in python means  we can chnage element of list in python and list follow ordering 
# mostly used (more than tuple also)
list=[1,2,3,4,5,6]
for i in list:
    print(i)

# list also follows negative indexing where last element of list is get by index as -1
print(list[-1])

# In append,we can entered element into last at last position
list.append(-1)
print(list)

# with insert method
list.insert(1,0)
print(list)

#  we can remove element in python by providing element value in remove element,and by providing index in pop method and if we dont provide index then last element will be removed
list.remove(-1)
print(list)
list.pop()
print(list)
list.pop(5)
print(list)

# copying a list in python and got to know that when we do list.copy() then shallow copy is created. here if we make change in duplicate one then original will not be affected because currently list containing unmutable objects.in this case Integer
print("perform operation of copying list in python")
a=[1,2,3,6,8,4,5]
b=a.copy()
print(a.sort())
print(b)
b[0]=10
print(a)
print(b)
#  so in below code ..both copies are affected because list contain mutable obj like nested list,dictionaries,set
a=[[10,20],[30,40]]
b=a.copy()
b[0][1]=15
print(a)
print(b)
print(type(b))

# join two list in python
list1=["a","b","c"]
list2=[1,2,3,4,5]
list3=list1+list2
print(list3)

# there is also another way of adding two list in java
list1=["a","b","c"]
list2=[1,2,3,4,5]
for i in list2:
    list1.append(i)
print(list1)

# we can also merge two list by using extend method
list1=["a","b","c"]
list2=[1,2,3,4,5]
list1.extend(list2)
print(list1)
print(min(list2)) #to find min element in list2
print(max(list2)) #to find min element in list2
print(f"sum of all numbers present in list2 is {sum(list2)}")
print(list2.reverse)