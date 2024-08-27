#Encapsulation

""" Encapsulation is a process of wrapping data and methods in a single unit. It is used to protect the data from the
outside world.

Types of Encapsulation :
*public
*private
*protected

"""

# public

class employee:

    def __init__(self):
        self.name="ram"
        self.age=35
        self.salary=65000

    def myfun(self):
        print("My name is",self.name)

x=employee()
x.myfun()
print(x.name)