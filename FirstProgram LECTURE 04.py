dict = {
    "key" : "value",
    "name" : "DHRUV",
    "learning" : "python",
    "age" : 17,
    "is_adult" : "NO",
    12 : 98.6,
    "syn" : ["bro", "brother", "bhai"],
    "SM" : ("ig", "wa", "tg", "x"),
    23.5 : 76,
    "true" : 1
}

print(dict)
print(type(dict))

# Dictionaries are unordered(on indexing) & mutable

print(dict["is_adult"])
print(dict["SM"])

dict[12] = 90.2
dict["surname"] = "patel"
print(dict)

# we may also creat a null dictionary

# Nested Dictionary
student = {
    "name" : "DHRUV PATEL",
    "subjects" : {
        "PHYSICS" : 65,
        "CHEMISTRY" : 81,
        "MATHS" : 73
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["MATHS"])

myDict = {
    "DHRUV" : "KANSARAKUI",
    "RUDRA" : "DELA",
    "JEEL" : "BHAVNAGAR",
    "ZEEL" : "RANSIPUR",
    "RAJ" : "VIRTA",
    "KUSHAL" : "VISNAGAR"
}

print(myDict.keys())
print(myDict.values())
print(myDict.items()) # Return (key,value) pairs as tuple
print(list(myDict.keys()))
print(tuple(myDict.keys()))
print(len(myDict)) # length of no. of keys
lt = list(myDict.keys())
print(lt[0])

print(myDict["JEEL"])
print(myDict.get("JEEL"))

#print(myDict["JEEl"]) # printing mistake here give error
print(myDict.get("JEEl")) # printing mistake here give none will be printed

myDict.update({"SAMEER" : "SUNSHI"})
print(myDict)

NEW = {"MEGH" : "BADARKHA"}
myDict.update(NEW)
print(myDict)

SET = {1, 2, 3, 4, 4, 2, 2, 2, "hi", "keep it up", "hi", 9}

print(SET)
print(len(SET))
print(type(SET))

# both dictionary and set are cobvered by {} so to create empty set
a = {} # this is empty dictionary
print(type(a))

b = set() # this is empty set
print(type(b))

#SET IS MUTABLE we may add element in it BUT ITS ELEMENTS ARE IMMUTABLE we can't change their values

b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(3)
b.add(6)
b.add(7)
b.add(8)
b.add(9)

print(b)

b.remove(2)

b.add("numbers")
b.add((6, 7, 8)) #tuple can be added but list cant

print(b)
print(len(b))

play = {"cricket", "volleyball", "chess", 3}

print(b.union(play))
print(play.intersection(b))

print(b.pop()) 
print(b.pop())
# removes random value
print(len(b))
print(b)

b.clear() # empties set
print(len(b))
print(b)

wap1 = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}
print(wap1)

wap2 = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print(len(wap2))
print(wap2)

'''
wap3 = {}

che = int(input("marks :"))
wap3.update({"che" : che})

phy = int(input("marks :"))
wap3.update({"phy" : phy})

math = int(input("marks :"))
wap3.update({"math" : math})

print(wap3)
'''

wap4 = {9, "9.0"}
print(wap4)

wap4 = {("int", 9),("float", 9.0)}
print(wap4)