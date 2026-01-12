a = 4
print(type(a))

comp=complex(8,2)
print('the value is ',a+comp,'and the type is',type(a+comp))

b=True
print('the type of a is',type(b))

c=None
print(type(c))

s="Harry"
t="kanha"
# print(a+s) only possible if same datatype
print(s+' '+t)  #when using  + then we have to manually add space

print(type(str(31)))
print(type(int("31")))

# i=input("Enter your age :")  #input always returns string
# print(type(i)) ==> string

i=input("Enter first no: ")   #12
j=input("Enter second no: ")    #100
print(i+j) #12100 because it returns string

name = "Abhishek"
age = 21
# automatically space assigned when using ,
print("My name is", name,"and i am",age,"years old") 

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # Value equality
print(a is b)   # Identity check


import copy

lst1 = [[1, 2], [3, 4]]
lst2 = copy.copy(lst1)
lst3 = copy.deepcopy(lst1)

lst1[0][0] = 99

print(lst2)
print(lst3)
