multiply=lambda x,y:x*y
print(multiply(2, 3))  # Output: 6

# using map function with lambda which works on each item in the iterable(list,tuples)
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# using filter function on specific items in the iterable by filtering them with a condition
numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # Output: [2, 4]

# using sorted function which returns a new sorted list from the elements of any iterable
words = ["apple", "banana", "cherry", "date"] 
sorted_words = sorted(words, key=lambda word: len(word)) #sorting according to the length
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

points = [(2, 3), (4, 1), (1, 5)]
sorted_points = sorted(points, key=lambda point: point[1]) #sorting accord to sec element
print(sorted_points)  # Output: [(4, 1), (2, 3), (1, 5)]

from functools import reduce

numbers = [1, 2, 3, 4, 5]
# Using reduce to calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (values/content are the same)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False (they are two different lists in memory)
c = a
print(a is c)  # True (c points to the exact same object as a)


a = 5
b = 5
print(a is b)  # True (since 5 is immutable so only one location will be created for it )

a="harry"
b="harry"
print(a is b)  # True because strings are also immutable so both a and b will point to same location of harry