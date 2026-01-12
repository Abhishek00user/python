animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     # using positive indexes
print(animals[-8:-1:2]) # using negative in dexes or use [1:9:2]

# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operations on that list and convert it back to a tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) #('apple', 'banana', 'cherry', 'orange') 

print(5/3)  #it returns float value 
print(5//3) #floor value
import math
print(math.ceil(7/3))

thistuple = ("apple",)
print(type(thistuple))  #tuple

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #string

# unpacking a tuple
info = ("Marcus", 20, "MIT")
(name, age, university) = info
print("Name:", name)
print("Age:", age)
print("Studies at:", university)

#But what if we have more number of items than the variables? use  *
fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna
print("Animals:", animals) #Animals: ['cat', 'dog', 'horse', 'pig']
print("Bird:", bird)        #Bird: parrot
print("Fish:", fish)        #Fish: salmon

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2  #If you want to multiply the content of a tuple
print(mytuple)  #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')