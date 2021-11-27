"""
project: House
version: 1.0
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"Furniture {self.name} occupies {self.area}"


class House:
    def __init__(self, house_type, area, item_list=None):
        if item_list is None:
            item_list = []
        self.item_list = item_list
        self.house_type = house_type
        self.area = area
        self.free_area = self.area
        for i in item_list:
            self.free_area -= i.area

    def __str__(self):
        output = f"House of type {self.house_type} has {self.free_area} free area out of {self.area} and contains "
        if not self.item_list:
            output += "nothing"
        for i in range(len(self.item_list)):
            if i == len(self.item_list) - 1:
                output += " and a " + self.item_list[i].name + " occupying " + str(self.item_list[i].area) + " area"
            elif i != 0:
                output += ", a " + self.item_list[i].name + " occupying " + str(self.item_list[i].area) + " area"
            else:
                output += "a " + self.item_list[i].name + " occupying " + str(self.item_list[i].area) + " area"

        return output

    def add_item(self, item):
        self.item_list.append(item)
        self.free_area -= item.area


house = House("Duplex", 100)
table = HouseItem("table", 10)
chair = HouseItem("chair", 5)
bed = HouseItem("bed", 20)

print(house)
house.add_item(table)
house.add_item(chair)
house.add_item(bed)
print(house)
