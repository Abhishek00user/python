def greet(name):
    print("Hello" , name)

greet("shah")

# printing a table of 5
def printTable_of_5():
    for i in range(1,11):  #11 is exclusive
        print(f"5 * {i} = {5*i}")   #here f in the print statement means that it is an formatted string that 
        # means even inside the curly braces we can update i and  5*i

printTable_of_5()