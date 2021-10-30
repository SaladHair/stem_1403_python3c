"""
instance or object of a class
"""

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("sleep() is called")

    def eat(self):
        print("eat() is called")


# main program
# tom = Cat()
tom = Cat("Tom", 1)
# reference name

tom = None
tom = 1
tom = 2
tom = "abc"
# garbage
