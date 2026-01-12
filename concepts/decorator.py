def greet(func):
    def wrapper():
        print("Before executing  function")
        func() #this is hello function written below
        print("after execting  function")
    return wrapper

#decorators(greet()) wrap original function with another function and original function (hello()) 
# still runs but only inside the decorator's wrapper

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
        return result
    return wrapper

@my_decorator
def greeting(name):
    print(f"Hello {name}!")

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
