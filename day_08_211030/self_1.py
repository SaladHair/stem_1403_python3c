"""
Adding attributes to an object
"""


# defining a class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.color does not exist

    def sleep(self):
        print("sleep() is called")

    def eat(self):
        print("eat() is called")
        print(f"{self.name} in eat()") # accessing attributes


# main program
tom = Cat("Tom", 1)
# print(tom.color)
# AttributeError: 'Cat' object has no attribute 'color'

tom.color = "Orange"
print(tom.color)

tom.eat()
