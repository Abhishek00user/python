# we have to replace all Java word with Python in a text file
with open("practise.txt","r") as f:
    data=f.read()
    new_data=data.replace("Java","Python")
     
with open("practise.txt","w") as f:
       f.write(new_data)

# we have to check if a particular word exist in the file or not
# def check_for_word():
#       word="Python"  
#       with open("practise.txt","r") as f:
#             data=f.read()
#             if(word in data):
#                   print("Found")
#             else:
#                   print("Not Found")  
# check_for_word()

# we have to write a program in which we have to tell about the  line wherre the 
# particular word occurs first  ,print -1 if not found
def check_for_line():
      word="is"
      data=True
      line_no=1
      with open("practise.txt","r") as f:
            while data:
                data=f.readline()
                if(word in data):
                    print(line_no)
                    return
                line_no+=1
                
      return -1
check_for_line()