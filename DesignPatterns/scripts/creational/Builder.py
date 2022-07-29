# Reference: https://github.com/faif/python-patterns/blob/master/patterns/creational/builder.py


# Abstract Building
class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big"


# Concrete Buildings
class Flat(Building):
    def build_floor(self):
        self.floor = "More than One"

    def build_size(self):
        self.size = "Small"


class ComplexBuilding:
    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big and fancy"


# construct
def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


if __name__ == "__main__":
    house = House()
    print(house)  # Floor: One | Size: Big
    flat = Flat()
    print(flat)  # Floor: More than One | Size: Small
    complex_house = construct_building(ComplexHouse)
    print(complex_house)  # Floor: One | Size: Big and fancy
