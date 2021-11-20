class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} weighs {self.weight}kg"

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


peter = Person("Peter", 75)
print(peter)

peter.run()
print(peter)

peter.eat()
print(peter)

