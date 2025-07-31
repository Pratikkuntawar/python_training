set={1,2,3,4,5}
# make use of set to create empty set
set.add(5)
print(set)
set.remove(5)
print(set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1 | set2) #union of set1 and set2
print(set1 & set2) #intersection of two set
print(set1-set2) #remove set2 elements from set1

# by two methods ,you can remove element from set 
# 1 by remove method and another one by discard method
set1.discard(10)# remove method will raise error if passed element is not present in set but discard method will not show any error
print(set1)