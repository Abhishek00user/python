x=input("Enter number 1: ")
y=input("Enter number 2: ")
try:  # Code that may cause an error
    z=int(x)/int(y)
    # a='baby yoda' + 56 # will lead to type error

except ZeroDivisionError as z:  # Code that runs if the error happens
    print("Exception occured:",z)
    z=0
    print("divison is ",z)

except TypeError as t:
    print("Exception occured: ",t)

except ValueError as v:  #when we give string as input instead of int
    print("Incorrect type",v)

else:  #else runs if no exception occurs.
    print('No exception occured')

finally:  #always runs, even if an error occurs
    print("executing finally whether exception occurs or not")

# raising custom error
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be at least 18")
#     return "Valid age"

# check_age(17)