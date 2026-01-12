# instance method ( can access instance and class variable both by using self)
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s = Student("Rahul")
s.show()



# class method ( can modify class variables and uses cls)
class Employee:
    company = "Google"

    @classmethod  # can access class variables only
    def change_company(cls, new_name):
        cls.company = new_name

Employee.change_company("Microsoft")
print(Employee.company)


# static methods(Static methods are logically related to a class but don’t access instance or class data.)
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 4))
