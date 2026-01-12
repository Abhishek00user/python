list=[2,1,3]
list.append(4)  #these functions doesn't return anything
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

#sorting also applies on words 

list.insert(1,10)
print(list)

list.reverse()
print(list)

# add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

# add a tuple to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = ("Mercedes", "Volkswagen", "BMW")
cars.extend(cars2)
print(cars)

# add a dictionary to a list
students = ["Sakshi", "Aaditya", "Ritika"]
students2 = {"Yash": 18, "Devika": 19, "Soham": 19}    # only add keys, does not add values
students.extend(students2)
print(students)

colors = ["voilet", "indigo", "blue", "green", "blue","yellow"]
colors.remove("blue")
print(colors)

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:4] = ["juan", "Anastasia"]  #2nd and 3rd index replaced and items after them added in last
print(names)  

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]  #2nd index will be replaced
print(names) 
print(names.index('juan'))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

