# Immutable = “once an object is created, its contents cannot be changed in place.”
# Any operation that looks like it “modifies” a string actually creates a new string object and leaves the old one untouched.

s = "hello"
print(id(s))             # memory id of 'hello'

s2 = s.replace("h", "y")
print(s2)                # 'yello'
print(id(s2))            # different memory id
print(s)                 # still 'hello'
print(id(s))             # same as before


print('He said, "I want to eat an apple".') 
print("it's fine")
print('c:\\users')  #c:\users
print('Hello\nWorld') #for new line if space between \n and W then space will be given at the starting of next line
print('Hello\tworld') #add 3 spaces
# print('He said, 
# "I want to eat an apple".')  it will throw error as triple quote needed in multiline string

# multiline string
receipe = """  
1. Heat the pan and add oil
2. Crack the egg
3. Add salt in egg and mix well
4. Pour the mixture in pan
5. Fry on medium heat
"""
print(receipe)

name="harry"
print(name[:3])
print(name[:-3])
print(name[0:])
print(name[-2:])

# methods
s=" apna college "  #remove spaces before and after string
print(str.strip(s))

str = "Hello !!!"
print(str.rstrip("!"))

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

str2 = "Silver Spoon"
print(str2.split(" "))  # Splits the string at the whitespace " ".


str3="i am studying python from apna college"
# capitalize function is making changes by creating a new string rather than in the str
print(str3.capitalize()) 
print(str3) 

# to avoid this 
str="i am studying"
str=str.capitalize()
print(str)

# str[0]='B'  not possible because string is immutable
print(str.find("t"))

sr='pythonprogramming'
print(sr[::3])

letter='hey my name is {} and i am from {}'
country='India'
name='ronn'
print(letter.format(name,country))

print(f"Hey my name is {name} and i am from {country}")
