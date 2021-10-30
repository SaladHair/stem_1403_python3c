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
# 3 objects(instances)
# tom = Cat("Tom", 1)
# fred = Cat("Fred", 1)
# peter = Cat("Peter", 2)

tom = Cat("Tom", 1)
fred = Cat("Tom", 1)
peter = Cat("Tom", 1)