# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r")
# data = f.read(4)
# print(data)
# print(type(data))
# f.close()

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)
# line5 = f.readline()
# print(line5)
# line6 = f.readline()
# print(line6)
# f.close()

# # Two types of write mode:- a--> Append: write at end , w--> Write: overwrite(delete previous and add new content from zero)

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","w")
# f.write("New content added.\nRemoved the old data.")
# f.close()

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","a")
# f.write("\nThis is appended data.\nYou may see it at end of old data.")
# f.close()

# # # If we open any non-existing file with a or w in python it makes one for us at given path.

# # f = open("..\I-O in py.txt","w")
# # f.close()

# # f = open("..\I-Oinpy.html","a")
# # f.close()

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","a+")
# f.write("\nNow I am trying both append and read at same time.\nOm is distracting me.")
# data = f.read()
# f.close()

# # r+ --> It reads and replaces the word from starting according to new given words.
# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt", "r+")
# f.write("abc") # new was replaced by abc
# print(f.read()) # as abc was written so pointer was at newt word to it so abc was excluded in read
# f.close

# # f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt", "r+")
# # print(f.read()) # adding read before write adds the write content at the end of content already written as pointer comes to end after read function.
# # f.write("abc")
# # f.close

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","w+")
# f.write("Trying +w\n1st write then read mode")
# data = f.read()# first write and then read deletes old content and add completely new content you written also read will give empty line as pointer will be at end
# f.close()
# print(data)

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","w+")
# data = f.read()
# f.write("Trying +w again\nbut its read first then write")
# f.close()# this will give a large blank space as use of +w will delete all the data then reading it will have no content remain to print it.
# print(data)

# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","a+")
# data = f.read()
# f.write("\nThis is a+\nits read first then write")
# f.close()# this is giving blank line as append will move cursor at end of file 
# print(data)


# f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","a+")
# f.write("\nThis is a+ again\nbut its write first then read")
# data = f.read()#This also give you the blank space as after adding content by append pointer will be at end.
# f.close()
# print(data)

# with open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r") as f:
#     data= f.read()
#     print(data)

# with open("D:\\Sem 1\\git\\git-rebase\\Main.txt","w") as f:
#     data= f.write("This content is written using 'with' syntax\nUse of 'with' means no need of close file after operation")

# Deleting a file
# We need to import a external module or library called os(operating system)

# import os
# os.remove("D:\\Sem 1\\git\\git-rebase\\Main.txt")

#WAP 1
# with open("../practice.txt","w") as s:
#     s.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

# #WAP 2
# with open("../practice.txt","r") as s:
#     data = s.read()

# new_data =data.replace("Java", "Python")
# print(new_data)

# with open("../practice.txt","w") as s:
#     s.write(new_data)

# #WAP 3
# word = "learning"
# with open("../practice.txt","r") as s:
#     data = s.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")

# def check_for_word():
#     word = "learning"
#     with open("../practice.txt","r") as s:
#         data = s.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not found")

# #WAP 4
# def check_for_line():
#     word = "programming"
#     line = True
#     line_no = 1
#     with open("../practice.txt","r") as s:
#         while line:
#             line = s.readline()
#             if(word in line):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()

#WAP 5
with open("../practice.txt","r") as s:
    data = s.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

count = 0
with open("../practice.txt","r") as s:
    data = s.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)