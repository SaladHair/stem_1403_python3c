"""
instance or object of a class

accessing instance attributes
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
# creating multiple instances
tom = Cat("Tom", 1)

# accessing instance attributes
name = tom.name
age = tom.age
print(name, age)
print(f'{tom.name}, {tom.age}')

# flow
tom.sleep()
tom.eat()