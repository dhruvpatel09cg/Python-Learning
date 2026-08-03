a = 1
while a <= 5:
    print("good morning guys")
    a += 1

print("loop ended")
print(a)

b = 1
while b <= 5:
    print(b)
    b += 1
print("loop ended")

c = 5
while c >= 1:
    print(c)
    c -= 1
print("loop ended")

d = 1
while d <= 100:
    print(d)
    d += 1

e = 100
while e >= 1:
    print(e)
    e -= 1

f = 1
while f <= 10:
    print(3 * f)
    f += 1

'''
g = 1
h = int(input("any no. you like:"))
while g <= 10:
    print(h * g)
    g += 1
'''

#traverse
i = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
j = 0
while j < len(i):
    print(i[j])
    j += 1

k = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
l = 49

m = 0
while m < (len(k)):
    if (k[m] == l):
        print("found at index" , m)
    else:
        print('finding...')
    m += 1

# break for breaking point in between the condtion

n = 1
while n <= 5:
    print(n)
    if(n == 3):
        break
    n += 1

print("end of loop")

p = 36
o = 0
while o < (len(k)):
    if (k[o] == p):
        print("found at index" , o)
        break
    else:
        print('finding...')
    o += 1

print("that's the end of your loop")

# continue is used for skipping an index

q = 0
while q <= 5:
    if(q == 3):
        q += 1
        continue
    print(q)
    q += 1
print("loop changes...")

r = 0
while r <= 15:
    if(r%2 == 0):
        r += 1
        continue
    print(r)
    r += 1