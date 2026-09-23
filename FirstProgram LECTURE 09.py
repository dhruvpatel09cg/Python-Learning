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