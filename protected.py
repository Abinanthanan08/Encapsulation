#protected

"""
In protected members of the class cannot accessed from outside the class but it can be accessible within the class and
its subclass.
It is used _(underscore).
"""

#protected

class shop:
    def __init__(self):
        self.name="john"
        self.age=45
        self._account=52523467

    def customer(self):
        print("Welcome",self.name,"how are you ?")
        print("My account no is",self._account)

b=shop()
b.customer()
#print(b.account)