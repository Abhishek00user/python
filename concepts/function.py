def name(fname,lname):
    print("hello",fname,lname)

name("sam","walker")

# default arguments
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# keyword arguments(no need to pass args in order)
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# arbitrary args
def name(*name):
    print("Hello,", name[0], name[1], name[2])
#  The function accesses the arguments by processing them in the form of a tuple.
name("James", "Buchanan", "Barnes")  

#keyword arbitrary args
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
# The function accesses the arguments by processing them in the form of a dictionary.
name(mname = "Buchanan", lname = "Barnes", fname = "James")  #ord

def add(a, b):
    return a + b
result = add(5, 3)
print(result)   # 8

def calc(a, b):
    return a + b, a - b, a * b
x, y, z = calc(10, 5)
print(x, y, z)   # 15 5 50

def greet():
    return    #If you don’t specify a value after return, the function returns None.
print(greet())   # None

# If a function has no return statement, it automatically returns None.

def test():
    print("Before return")
    return "Done"
    print("After return")  # ❌ never executed
print(test())

