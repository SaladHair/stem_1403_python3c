"""
instance or object of a class
identity
id()
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
fred = Cat("Tom", 1)
peter = Cat("Tom", 1)

print(id(tom))
print(id(fred))
print(id(peter))

# 1364038062032
# 1364038061840
# 1364038061024

print("=========")
tomma = tom

print(id(tomma))
print(id(tom))
# 1615631314896
# 1615631314896