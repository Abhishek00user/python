# Generator expression
# This creates a generator object which uses next keyword and yield keyword
def gen_numbers():
    yield 1
    yield 2
    yield 3

g = gen_numbers()
print(g)           # <generator object ...>
print(next(g))     # 1
print(next(g))     # 2
print(next(g))     # 3
# next(g) #would raise StopIteration

squares_gen = (x**2 for x in range(5))
# Convert to list to see values
# print(list(squares_gen) ) # [0, 1, 4, 9, 16]
print(next(squares_gen))    #0
print(next(squares_gen))    #1
print(next(squares_gen))    #4
print(next(squares_gen))    #9
print(next(squares_gen))    #16
# print(next(squares_gen))  can't be reused after getting exhausted it will raise an exception

# list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0] # Result: [0, 4, 16, 36, 64]

# dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0} # Result: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# set comprehension
unique_remainders = {x % 3 for x in range(10)}  # Result: {0, 1, 2}

# nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row] # Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

words=['hello','hii','there']
upperF=[word.upper() for word in words]  #Result: ['HELLO', 'HII', 'THERE']

