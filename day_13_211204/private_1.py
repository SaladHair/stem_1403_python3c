"""
private member
private attribute

delegator accesses private attributes
"""


class Animal:
    def __init__(self, name):
        self._name = name
        self.age = 1


# test
dog1 = Animal("Husky")

print(dog1.age)
print(dog1.name)

# dog1.name = "Peter"
# print(dog1.name)
