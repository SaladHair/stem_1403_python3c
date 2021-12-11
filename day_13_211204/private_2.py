"""
private member
private attribute

delegator accesses private attributes
"""


class Animal:
    def __init__(self, name):
        self._name = name
        self.age = 1

    def getName(self):
        # read private attribute
        return self._name

    def setName(self, newName):
        # write private attribute
        self._name = newName


# test
dog1 = Animal("Husky")

# get the name of the dog
print(dog1.getName())

# rename the dog
dog1.setName("Peter")
print(dog1.getName())
