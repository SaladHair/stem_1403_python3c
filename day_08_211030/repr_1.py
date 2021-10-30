"""
__str__()
__repr__()
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

    def __repr__(self):
        # print('__str__() is called')
        # TypeError: __str__ returned non-string (type NoneType)
        objinfo = self.__class__.__name__ \
                  + "[" \
                  + "name=" \
                  + self.name \
                  + ", age=" \
                  + str(self.age) \
                  + "]"
        return objinfo


#
tom = Cat("Tom", 1)

# print info
print(tom.name)
print(tom.age)

# print(tom)

print(repr(tom))
