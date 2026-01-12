d = {
    "name" : "Apna College" ,
    "subjects": ["python","javascript"] ,
    "topics" : ("dict","sets") ,
    "age" : 35,
    "is_adult" : True
}
print(len(d))

# the dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

null_dict={}  # null dictionary
# print(dict["subjects"]) 
d["name"]="nothing"  #modified or mutated by overwriting
d["surname"]="Raj"  #new key valur pair added
print(d)

info = {'name':'Karan', 'age':19, 'eligible':'yes'}
print(info['name'])         #karan
print(info.get('eligible'))  #yes
print(info.values())        #dict_values(['Karan', 19, 'yes'])
print(info.keys())          #dict_keys(['name', 'age', 'eligible'])
print(info.items())         #dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
info.update({'DOB':2001})  #The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value 

#nested dictionaries
student={
    "name":"Abhishek",
    "subjects": {
        "maths": 87,
        "chemistry":90
    }
}
print(student)
print(student["subjects"]["maths"])  #87
for key, value in student.items():
    print(key, ":", value)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# below loop (works fine when values are dictionaries)
for x, obj in myfamily.items():
    print(x)    
    for y in obj:
        print(y + ':', obj[y])


student = {
    "name": "Alice",
    "marks": {
        "math": 90,
        "science": 85
    }
}
student.update({"age": 20})  #Add a new key to outer dictionary
print(student)
# {'name': 'Alice', 'marks': {'math': 90, 'science': 85}, 'age': 20}

student["marks"].update({"english": 88})  #Add a new key to nested dictionary
print(student)
# {'name': 'Alice', 'marks': {'math': 90, 'science': 85, 'english': 88}, 'age': 20}

student["marks"].update({"history": 75, "geography": 80})  #Update multiple values at once
print(student)
# {'name': 'Alice',
#  'marks': {'math': 90, 'science': 85, 'english': 88, 'history': 75, 'geography': 80},
#  'age': 20}
