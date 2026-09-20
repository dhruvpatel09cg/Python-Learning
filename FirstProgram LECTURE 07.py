f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r")
data = f.read(4)
print(data)
print(type(data))
f.close()

f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5)
line6 = f.readline()
print(line6)
f.close()

# Two types of write mode:- a--> Append: write at end , w--> Write: overwrite(delete previous and add new content from zero)

f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","w")
f.write("New content added.\nRemoved the old data.")
f.close()

f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","a")
f.write("\nThis is appended data.\nYou may see it at end of old data.")
f.close()

# # If we open any non-existing file with a or w in python it makes one for us at given path.

# f = open("..\I-O in py.txt","w")
# f.close()

# f = open("..\I-Oinpy.html","a")
# f.close()

f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt","a+")
f.write("\nNow I am trying both append and read at same time.\nOm is distracting me.")
data = f.read()
f.close()

# r+ --> It reads and replaces the word from starting according to new given words.
f = open("D:\\Sem 1\\git\\git-rebase\\Main.txt", "r+")
f.write("abc")
f.close