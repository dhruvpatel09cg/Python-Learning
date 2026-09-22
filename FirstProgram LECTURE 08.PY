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
    #default constructor
    def __init__(self):
            pass

    #parameterized constructor
    def __init__(defg, name, marks):
        defg.name = name #It is not necessary to call the object 'self' we may call it anything but, self is general way
        defg.marks = marks
        print("Adding new student in database...")

s1 = Student("Karan", 94) #this parenthesis calls the constructor
print(s1.name, s1.marks)
print(s1)

s2 = Student("Jeel", 95)
print(s2.name, s2.marks)
print(s2)

# only the one constructor which satisfies the format of object will run like here default will not run.

