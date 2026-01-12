thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #add one element at a time
print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #use update for add multiple items from another set into the current set
# So after the update you have one set of strings — you do not have {"apple", "banana", "cherry", {"pineapple", "mango", "papaya"}} (a set containing another set).
print(thisset)

# frozenset is immutable version of a set i.e,we can't add or remove elements (it can be used as key in dict)
s = {1, 2, 3}                # normal set
f = frozenset([1, 2, 3])     # frozenset from a list
g = frozenset({3, 4, 5})     # frozenset from a set
print(s)  # {1, 2, 3}
print(f)  # frozenset({1, 2, 3})
print(g)  # frozenset({3, 4, 5})


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# set3 = set1 | set2  this can also be used
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)  #or use  myset = set1 | set2 | set3 |set4
print(myset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #The update() changes the original set, and does not return a new set.
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2  we can also use this 
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2) 
print(set3)  # {False, 1, 'apple'} as false is equivalent to 0

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
# set3 = set1 - set2
print(set3)     #{'banana', 'cherry'}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)  #updates original set
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2
print(set3)     #{'cherry', 'microsoft', 'banana', 'google'}  apple not included as it is present in both set

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))  #return false even if one of the item is common

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities.issuperset(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))