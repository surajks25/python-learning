# file input/output in python
# python can be used to perform operation on a file (read & write data)

# type of all files
# text file: txt, docx , log, etc
# binary file: mp4, mov, png, jpeg etc

# f = open('file_name","mode')

# sample.txt      r:read mode
# demo.docx       w:write mode

# file = open("day7Demo.txt", "r") #day7Demo.txt this is my text file i create inside same folder so you need to confirm the location of current file then only it will work
# data = file.read()
# print(data)
# print(type(data))
# file.close()

#diff char and meaning
# r open for reading default
# w open for writing truncating the file first
# x create a new file and open it for writing 
# a open for writing appending to end of the file if it exist
# b binary mode
# t text mode(default)
# + open the disk file for updating (reading and writing)


# file = open("day7Demo.txt", "rt") # rt also workig coz t default
# data = file.read()
# print(data)
# print(type(data))
# file.close()

# r read
# r+ read and write
# w write
# w+ write and read
# a append
# a+ append and read

# # particular letter we want to print
# file = open("day7Demo.txt", "rt") 
# data = file.read(3) #it will print only the letters of three
# print(data)
# file.close()

# # line by line read the letters
# file = open("day7Demo.txt", "rt") 
# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)
# file.close()

# writing to a file
# f = open("demo.txt", "w") write mode
# f.write("this is a new line")

# f = open("demo.txt", "a") append mode add at the end
# f.write("this is a new line")

# f = open("day7Demo.txt", "a")
# f.write("\n this is a new ddd line") #mext also come
# f.close()

# #if we dont have text file just type below code it will atomatically cretea on text file
# fa = open("sample.txt", "w") #we use w and a also both are same new file creation #it will createa new one we dont need to create a new file
# fa.close()

# file = open("sample.txt", "r+") #read and write both
# file.write("haii") #overright the already existing text
# file.close()

# file = open("sample.txt", "w+")# this will delete hole text inside the sample.txt like truncate
# print(file.read())
# file.close() 

# file = open("sample.txt", "w+")
# print(file.read())
# file.write("haii my name is suraj")#work both read and write first truncate hole data and write another data
# file.close() 

# file = open("sample.txt", "a+") #added another line
# print(file.read())
# file.write("\nhaii my name is suraj\n")
# file.close() 

# recall
# r+ read and overwrite (pointer start) - no tuncate
# w+ read and overwrite                 - truncate
# a+ read and append    (pointer end)   - no truncate

# with syntax
# with open("demo.txt", "a")as f: as is alias
#     data=f.read()
# with open("sample.txt", "r") as f: # this syntax no need of any type closing arguments like file.close()
#     data = f.read()
#     print(data)

# with open("sample.txt", "w") as f:
#     f.write("this is with using re write the text")

# deleting a file
# using the os module
# module like a code library is a file written by another programmer that generally has a function we can use. 
#
#  import os
# os.remove(filename)

#like import tensorflow, import seaborn,
#if you dont have a library you need to install like this pip install tensarflow etc

# inbuit function inside the os library
# import os
# os.remove("sample.txt")

# practise q 
# file = open("practise","w")
# file.write("Hi everyone \nwe are learig file i/o \nusing java i like programming in java")
# file.close()

# another way add data
# with open("sample.txt", "w") as f:
#     f.write("Hi everyone \nwe are learig file i/o \nusing java i like programming in java")

# replace the word java to py, first we read the data and overright
# with open("sample.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("java", "python")
# print(new_data) 
# # THIS ABOVE code just change text and print only a terminal so we need to change in txt file also so we need below code
# with open("sample.txt","w") as f:
#     f.write(new_data)

# cheack if the word is exist in the text file or not word = learning
word = "learning"
with open("sample.txt", "r") as f:
    data = f.read()
    if data.find(word) != -1:
        print("found")
    else:
        print("not found")
