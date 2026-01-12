f=open("demo.txt","r")
data=f.read()
# if we want to read only first 10 letters then we can write f.read(10)
print(data)
f.close()
# once the whole file has been read then the pointer has came to the last of file
# now readline function below will not work 


f=open("demo.txt","r")
line1=f.readline() #for reading the first line
print(line1)
line2=f.readline() #reading the second line
print(line2)
f.close()


# Overwriting to a file
f=open("demo.txt","w")  #overwrites the file by deleting the old content and adding new content
f.write("existing value in demo.txt has been overwritten \nor truncated")
f.close()
# for checking if changes have been made 
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()


# # adding to the last  of the file
f=open("demo.txt","a")
f.write("\nnew data has been appended to the existing data")
f.close()


# if we open a file which has not been created yet then a new file will be 
#automatically get created and if it exist then it truncate first then writes
f=open("autoCreated.txt","w")
f.write("this file has been automatically created ")
f.close()

# using r+  overwriting will be done but overwriting will start from the beginning of the file
f=open("demonstr.txt","r+")
f.write("that")  #that has been overwritten to the starting word "this" which was prev written in the file 
# now pointer moves forward i.w, if we read the file now then 'that' will not be read 
print(f.read())
f.close()

# using w+  whole content will be overwritten 
f=open("wplus.txt","w+")
f.write("prev content of the file has been truncated")
print(f.read())  #pointer has moved to the last that's why nothing is going to be printed
f.close()

# using a+
f=open("aplus.txt","a+")
print(f.read())   #nothing will pe printed because stream is at the end of file
f.write("\nnew content")  #appended

f.close()

# another syntax for all this
with open("anothSyn.txt","r") as f:
    data=f.read()
    print(data)
#     no need to close the file as it get automatically closed

#how to delete the file
import os
os.remove("")