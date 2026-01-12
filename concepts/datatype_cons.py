# Using list()
lst1 = list()                      # empty list → []
lst2 = list([1, 2, 3])             # from another list → [1, 2, 3]
lst3 = list("hello")               # from string → ['h', 'e', 'l', 'l', 'o']
lst4 = list((10, 20, 30))          # from tuple → [10, 20, 30]
lst5=list({10,200,0})

# Using tuple()
t1 = tuple()                       # empty tuple → ()
t2 = tuple([1, 2, 3])              # from list → (1, 2, 3)
t3 = tuple("abc")                  # from string → ('a', 'b', 'c')
t4 = tuple({10, 20, 30})           # from set → (10, 20, 30) [order may vary]

# Using set()
s1 = set()                         # empty set → set()
s2 = set([1, 2, 3, 3])             # from list → {1, 2, 3}
s3 = set("hello")                  # from string → {'h', 'e', 'l', 'o'}
s4 = set((10, 20, 20, 30))         # from tuple → {10, 20, 30}

# Using dict()
d1 = dict()                        # empty dict → {}
d2 = dict(a=1, b=2)                # keyword args → {'a': 1, 'b': 2}
d3 = dict([("x", 10), ("y", 20)])  # from list of tuples → {'x': 10, 'y': 20}
d4 = dict(zip(["name", "age"], ["Alice", 21]))  # from zip → {'name': 'Alice', 'age': 21}
