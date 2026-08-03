marks = [95.5, 46.8, 76.8, 69.8, 89.5, 79.3]
print(marks)
print(type(marks))

print(marks[0])
print(marks[4])

print(len(marks))
#we may store different types (int, float, str etc.)

student = ["DHRUV", 98, "KANSARAKUI", "CRICKET"]

print(student[3])

'''
string is immutable but list is mutable
for eg.
str = "hello"
print(str[0])   , is possible but
str[0] = r , giving value is not possible.
and giving value is possible in list
'''
menu = ["ROTI", "DAL", "CHAWAL", "SABJI", "BUTTERMILK"]
print(menu)
menu[4] = "CUSTARD"
print(menu)
print(menu[3:5])
print(menu[-4:-2])

score = [303, 264, 319, 76, 140]
score.append(131) # APPEND = TO ADD
print(score)

score.sort() # gives list in ascending order
print(score)

score.sort(reverse=True) # for descinding order
print(score)

'''
if elements of list are in string form ascending = alphabetic
descending = reverse alphabetic
'''
score.reverse()
print(score)

menu.reverse()  # to reverse the list
print(menu)

score.insert(3,212) # to add at specific index
print(score)

score.remove(303) # to remove an element
print(score)

score.pop(5) # to remove from a specific index
print(score)

score.copy()
print(score)

# TUPLES

tup = (45, 63, 9, 72, 33, 93)
print(tup)
print(tup[1])
print(type(tup))
# tules are immutable so we cant replace its elements 

#for single element tuple we should end with , otherwise considered as integer
tup1 = (1)
print(tup1)
print(type(tup1))

tup2 = (1,)
print(tup2)
print(type(tup2))
print(tup[2:5])

print(tup.index(33))

li = [1,2,3,4,5]
li.append(7)
print(li)
# we have to use methods seperately in list
'''
print(tup.count(93)) 

Movies = []
mov1 = input("1st movie:")
mov2 = input("2nd movie:")
mov3 = input("3rd movie:")

Movies.append(mov1)
Movies.append(mov2)
Movies.append(mov3)

print(Movies)
'''
# PALINDROME [1,2,3,2,1] OR [RACECAR]

list1 = [1,2,3,4,5]
list2 = [1,2,3,2,1]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("non palindrome")

tup = ("c", "d", "a", "a", "b", "b", "a")
print(tup.count("a"))

list =  ["c", "d", "a", "a", "b", "b", "a"]
list.sort()
print(list)