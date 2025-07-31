# learn about tupels in list and got to know that tules are similar to list in python
# but tuples are unmutable data types cant support to add values,delete values and update values
# another simple diff between list and tupple in python is that list are denoted by sq brackets and tuple is denoted by () round brackets
tuple=(1,2,3,4,5,6)

print(tuple)
# tuple[0]=0.  this statement will give error 
print(tuple)
# empty tupple
t=()
print(type(tuple))
#  tuple also supports negative indexing
my_tuple=(10,20,30,40,50,40,30)
for i in my_tuple[::-1]:
    print(i,end=" ")
print()
print(my_tuple.count(30))
# count method will count ...how many times that element has been occured in tuple and index method will give index of first occurence
print(my_tuple.index(30))

# my_tuple.sort().  tupple does not support sort() function because tuple is immutable data structure and thats why it does not support sorting function
print(my_tuple)