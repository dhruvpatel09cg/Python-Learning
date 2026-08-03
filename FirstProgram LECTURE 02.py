str1 = "This is a string.\nWe are creating it in python." 
#  \n stands for next line.
print(str1)
str2 = "This is a string.\tWe are creating it in python."
#  \t stands for a large space called tab space
print(str2)
name = "DHRUV"
surname = "PATEL"
full_name = name +" "+ surname
print(full_name)
print(name +" "+ surname)
# LENGTH OF STRINGS
print(len(name))
print(len(surname))
print(len(full_name))
print(len(str1))
print(len(str2))
# STRING INDEXING
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

'''
WHILE INDEXING STARTING INDEX ALWAYS INCLUDED AND ENDING 
INDEX EXCLUDED AND INDEXING START FROM 0
'''

worth = full_name[6:11]
print(worth)
# 11 IS ALSO CALLED len(str)
ok = full_name[0:len(full_name)]
print(ok)
# also if we leave unwritten it will be cosidered as the end 

eg = "we are learning python right now"
print(len(eg))
print(eg[:21]) # [0:21]
print(eg[3:]) # [3:32]

#NEGATIVE INDEXING:WHEN IDEX COUNTED BACKWARD STARTING FROM -1
print(eg[-3:])

print(eg.endswith("w"))
# if function ends with written = true otherwise false

print(eg.capitalize())
# capitals 1st charecter

print(eg.replace("python" , "java"))
# replaces (old , new)

print(eg.find("studying"))
print(eg.find("learning"))


'''
if word exists = gives index no. (positive value)
if word doesen't exist = gives -1
'''


print(eg.count("r"))
# counts how many time letter or character comes in string


money = "!@#$%^&*&%$##@$$$$#$%#%^"
print(money.count("%"))

#conditional statements
age = 21
if(age >= 18):
    print('eligible to vote')
    print('may have a licence')

jnvst = 'passed' 
if (jnvst == 'failed'):
    print('NO ADMISSION')
elif (jnvst == 'waitlist') :
    print('KEEP HOPE')
elif(jnvst == 'passed'):
    print('congratulations you nailed it')

# if every time checked and elif only checked when if is false

age = 13

if (age >= 18):
    print('can vote') # spacing 4 times before it called indentation
else:
    print("bachha hai abhi tu")

'''
marks = int(input("how many marks got:"))

if(marks >= 95):
    grade = "A+"
elif(marks >= 80 and marks < 95):
    grade = "A"
elif(marks >= 60 and marks < 80):
    grade = "B"
elif(marks >= 45 and marks < 60):
    grade = "C"
elif(marks >= 33 and marks < 45):
    grade = "D"
else:
    grade = "fail"

print("grade of student -->", grade)
'''

# nesting means an if statement inside an if statem

age = 87

# NESTING 
if(age >= 18):
    if(age >= 70):
        print("cannot drive")
    else:
        print("can drive")
else:
    print('cannot drive')

'''
num = int(input("any no.:"))

if(num % 2 == 0):
    print("even")
else:
    print("odd")
'''

'''    
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

if(a > b and a > c):
    print("a is greatest")
elif(b > c):
    print("b is greatest")
else:
    print("c is greatest")
'''

'''
num = int(input("enter a no.:"))
rem = num % 7

if(rem == 0):
    print(" multiple of seven")
else:
    print("not a multiple of seven")
'''