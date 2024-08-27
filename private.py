#private

"""
In private members of the class cannot accessed from outside the class but it can be accessible within the class.
It is used __ (double underscore).
"""

# private

class student:

    def __init__(self):
        self.name="vijay"
        self.age=18
        self.__reg_no=20101

    def cse(self):
        print("My age is",self.age)
        print("My reg_no is",self.__reg_no)

a=student()
a.cse()
#print(a.reg_no)