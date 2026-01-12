# constructor overloading using default arguments
class Teacher:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

# s1 = Student()
# s2 = Student("Rahul")
# s3 = Student("Rahul", 20)

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