# python does not support constructor overloading like java or cpp . the second __int__() will overwrite the first
# however we can do constructor overloading using default arguments, *args, **kwargs and class methods
class Teacher:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

# The same __init__  handles all three cases
t1 = Teacher()
t2 = Teacher("RN")
t3 = Teacher("sahu",34)

# using *args
class Student1:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "Unknown"
            self.age = 0

        elif len(args) == 1:
            self.name = args[0]
            self.age = 0

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]


s1 = Student1()
s2 = Student1("Abhishek")
s3 = Student1("Abhishek", 22)

# using kwargs
class Student2:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Unknown") # unknows is simply a default value that i choose
        self.age = kwargs.get("age", 0)
        self.city = kwargs.get("city", "Unknown")


s1 = Student2()
s2 = Student2(name="Abhishek")
s3 = Student2(name="Abhishek", age=22)
s4 = Student2(name="Abhishek", age=22, city="Delhi")
class Student:
    college_name="OiSt"  #class variable

    def __init__(self,name,marks): # instance variables
        self.name=name  #name has been created and we are passing fullname to the object's name
        self.marks=marks
        print("adding new student to the database with name and marks given below : ")
    
# methods for the class
    def welcome(self):
        print("welcome student, ",self.name)

    def get_marks(self):
        return self.marks

s1=Student("Abhishek",50) #abhishek passed to the fullname in init function
# print(s1.name,s1.marks)
print(Student.college_name)  #class attribute called with the help of class name
s1.welcome()
print(s1.get_marks())