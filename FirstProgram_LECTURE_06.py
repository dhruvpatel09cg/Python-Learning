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