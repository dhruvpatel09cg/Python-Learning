a = 4
b = 9

sum = a + b
print(sum)

#more lines of code

a = 2
b = 34

sum = a + b
print(sum)

#more lines of code

a = 6
b = 4

sum = a + b
print(sum)

# function definition
def calc_sum(a, b): #parameters
    sum = a + b
    print(sum)
    return sum

calc_sum(53, 64) #function call; arguments

# Also we may write like

def calcsum(a, b):
    return a + b

sum = calcsum(12, 34)
print(sum)

def print_hello():
    print("hello")

print_hello()

output = print_hello()
print(output) #printing a function with no return value will give none

def status():
    print("staged")
    return "up to date"

status()

commit = status()
print(commit)

# avg of 3 no.

def avg3(a, b, c):
    avg = a + b + c
    result = avg / 3
    print(result)

avg3(12, 13, 14)

#print is a built in function with some specs like always leaves a space and next print function will be in next line

print("Dhruv""patel")
print("Dhruv","patel"), print("Founder") #word still prints in next line
# to print in same line we should give end tag to something else

print("dhruv",end=" ")
print("patel")

print("dhruv",end="")
print("patel")

for i in range(2, 40, 10):
    print(i)
    i += 1

status()

def calc_prod (a=1, b=1):
    print(a * b)
    return a * b

calc_prod(7, 4)

# WAF 1
cities = ["Ahmedabad", "Delhi", "Mumbai", "Chennai", "Hyderabad", "Mehsana"]
hero = ["thor", "hawk eye", 4, "45"]

def print_len(list):
    print(len(list))

print_len(hero)
print_len(cities)

def print_element(list):
    for d in list:
        print(d, end=" ")

print_element(cities)
print()

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(9)

def converter(usd):
    inr = usd * 96
    print(usd, "$ =", "₹", inr)

converter(39)

# num = int(input("No.: "))
# for i in range(1):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# num = int(input("Num:"))
# if num%2 == 0:
#     print(num, "Even")
# else:
#     print(num, "Odd")


#--> Recursive Functions
# n = int(input("No.:"))
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("end") # used to understand call stacks
# show(n)

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(7))

def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) +n

ok = calc_sum(20)
print(ok)

subject = ["Py", "HTML", "CSS", "JS"]
def list_print(subject, idx=0):
    if (len(subject)==idx):
        return
    print(list[idx])
    print(subject, idx+1)

list_print(subject)