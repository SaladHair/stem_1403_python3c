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

    def live(self):
        # call other methods with self
        self.sleep()
        self.eat()


# main program
tom = Cat("Tom", 1)

tom.color = "Orange"
print(tom.color)

tom.live()
