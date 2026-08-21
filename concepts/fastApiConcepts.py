# args is used when we don't know how many arguments will be passed to a function. It is of type tuple and is used to pass
#  var no of arguments
def add(*args):
    total = 0

    for number in args:
        total += number

    return total

# kwargs is used when we don't know how many keyword arguments will be passed to a function. Is is of dict type
def calculate(**kwargs):
    total = 0

    for key, value in kwargs.items():
        total += value

    return total

res = calculate(a=1, b=2, c=3)  # returns 6
print(res)

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1, 2, 3, a=4, b=5)  # prints (1, 2, 3) and {'a': 4, 'b': 5}

# * and ** can also be used to unpack arguments when calling a function
numbers = (1, 2, 3)
res = add(*numbers)  # equivalent to add(1, 2, 3)
print(res)
