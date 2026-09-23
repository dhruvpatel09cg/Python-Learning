# class Student:
#     def  __init__(self, name):
#         self.name = name

# # Deleting object
# s1 = Student("Dhruv")
# print(s1.name)
# del s1.name
# print(s1.name)

# Private attributes & methods
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # Giving 2 __ before attribute make it private

    def reset_pass(self):
        print(self.__acc_pass) # This is valid as we are printing password inside a class

acc1 = Account("12345678", "D@p@tel09")
print(acc1.acc_no)
# print(acc1.acc_pass) # Printing private attribute will give error while running code.

acc1.reset_pass() # This will give the password ai password is printed inside a class

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__name)
# p1.__hello
p1.welcome()

# Inheritance
# --> Single Inheritance
class Car:
    @staticmethod # here we used staticmethod as start and stop of cars of every company(subclass) have same methods
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Land Cruiser 300")
car2 = Toyota("Vellfire")

print(car1.name)
car1.start()


# --> Multi-level inheritance
class Car:
    @staticmethod 
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class LC300(Toyota):
    brand = "Toyota"

    def __init__(self, f_type):
        self.f_type = f_type 

car1 = LC300("Petrol")
print(car1.f_type, car1.brand)

# --> Multiple Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

b1 = B()
print(b1.varB)

# Super Method
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = Toyota("Hilux", "Hybrid")
print(car1.name, car1.type)

# @classmethod
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name
        # Person.name = name
        # self.__class__.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

# line 131 & 132 are alternative of @classmethod
'''
We have 3 type of methods:
1] Static method ==> ()
2] class method ==> (cls)
3] instance method ==> (self)
'''

# @property
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.chem + self.phy + self.math)/3) + "%"

    # def calcper(self):
    #     self.percentage = str((self.chem + self.phy + self.math)/3) + "%" # This is alternative of @property

    @property
    def percentage(self):
        return str((self.chem + self.phy + self.math)/3) + "%"

s1 = Student(98, 89, 92)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage) # After using this the marks are changing but percentage remains as per old data

# s1.calcper()
# print(s1.percentage) # After using property no need to use this

'''@getter & @setter to study'''

# Polymorphism
# --> Operator Overloading
# function of different operator different according to different data type:
print(1 + 2) #Add
print("Dhruv " + "Patel") #concatenate
print([1, 2, 3] + [4, 5, 6]) #merge
# + did different function acc. to different data types

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img+ num2.img
        return Complex(newReal, newImg) # Alternate of Dunder

    def __add__(self, num2):
            newReal = self.real + num2.real
            newImg = self.img+ num2.img
            return Complex(newReal, newImg)

    def __sub__(self, num2):
                newReal = self.real - num2.real
                newImg = self.img - num2.img
                return Complex(newReal, newImg)

num1 = Complex(1, 4)
num1.showNumber()

num2 = Complex(6, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()

# num3 = num1.add(num2)
# num3.showNumber() #no need to use this after Dunder
# Dunder functions: used __ before

class Circle:
    def __init__(self, rad):
        self.rad = rad

    def Area(self):
        return 3.14*self.rad**2

    def Perimeter(self):
        return 2*3.14*self.rad

c1 = Circle(4)
print(c1.Perimeter())
print(c1.Area())

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(self.role)
        print(self.dept)
        print(self.salary)

e1 = Employee("Accountant", "Account", "₹90,000")
e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "₹6,20,000")

    def showDetails(self):
        print(self.name)
        print(self.age)

eng1 = Engineer("Dhruv","24")
eng1.showDetails()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("Chips", 20)
ord2 = Order("Hell", 60)

print(ord1 < ord2)
print(ord1 > ord2)