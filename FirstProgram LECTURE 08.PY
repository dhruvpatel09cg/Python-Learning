class Student:
    name = "Karan"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    color = "Blue"
    brand = "Mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

class Student:
    def __init__(self, fullname): #constructor
        self.name = fullname
        print("Adding new student in database...")

s1 = Student("Karan") #this parenthesis calls the constructor
print(s1.name)
print(s1)

s2 = Student("Jeel")
print(s2.name)
print(s2)

class Student:
    college_name = "ACB College" #we are saving data of students of same college so no need to assign it every time.
    name = "Anonymous" # --> class attribute
    #default constructor
    def __init__(self):
            pass

    #parameterized constructor
    def __init__(defg, name, marks):
        defg.name = name #It is not necessary to call the object 'self' we may call it anything but, self is general way
        defg.marks = marks # --> object attribute
        print("Adding new student in database...")

s1 = Student("Karan", 94) #this parenthesis calls the constructor
print(s1.name, s1.marks)
print(s1)

s2 = Student("Jeel", 95)
print(s2.name, s2.marks)
print(s2)

print(Student.college_name)
# only the one constructor which satisfies the format of object will run like here default will not run.
# if we have both class and object attribute with same name object attribute will be preferred like here name attribute. This is used for cases such that a student don't provide name

# --> Methods 
# classis made up of 2 things data(attributes) & methods |or| class may store attributes and methods

class Student: #Class
    college = "GEM College" #Class attribute
    def __init__(self, fullname, marks): #constructor
        self.name = fullname #Object attribute
        self.marks = marks

    def hello(self): # Method
        print("hello", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan", 85) #Object
s1.hello()
print(s1.get_marks())

# WAP
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is", sum/3)

s1 = Student("Rohit", [85,94,96])
s1.avg()

# --> Static Methods
# no need to use self and they work at class level
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #decorator
    def hello():
        print("hello")

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is", sum/3)

s1 = Student("Rohit", [85,94,96])
s1.hello()
Student.hello()

# Abstraction : Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started...")

car1 = Car()
car1.start()
# In above example the unnecessary steps which are not mandatory for user to know like acc True and clutch True are not shown that's what called Abstraction. We used in all the above examples.

# Encapsulation : Wrapping data and functions into a single unit (object).

# All the classes we created in this file till now are example of Encapsulation as they all wrapped each necessary methods and attributes in themselves.

# WAP
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        if amount<=self.balance:
            print("remaining balance",self.balance-amount)
        else:
            print("no enough money")
        self.balance -= amount

    def credit(self, amount):
        self.add = amount
        print("New balance:", self.balance+amount)
        self.balance += amount

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(7000)
acc1.debit(6000)
acc1.debit(20000)

# WAP
