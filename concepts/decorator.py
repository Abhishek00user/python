# A decorator is a function that takes another function, modifies or extends its behavior, and returns a function.
def greet(func):
    def wrapper():
        print("Before executing  function")
        func() #this is hello function written below
        print("after execting  function")
    return wrapper

# here the decorator name is greet and it has wrapped the hello function. So when we call hello(), it will first execute the wrapper function and then the hello function.

@greet     #decorator declaration , now hello points to the wrapper function returned byy decorator
def hello():
    print("executing function")

hello()

# If the function accepts arguments, you must pass them in the wrapper using *args and **kwargs:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result  # we are using return here because we want to return the result of the function call
    return wrapper

@my_decorator
def greeting(name,city='ara'):
    print(f"Hello {name} from {city}!")

greeting("Abhishek")

# Decorators can also modify the return value
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(5, 10))  # 30 instead of 15

from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # it first returns a decorator function and then the home function is passed to it as an argument. So when we call home(), it will first execute the decorator function and then the home function.
def home():
    return {"message": "Hello"}