#!/usr/bin/env python3
your_name = input("Hi! Whats your name?")
my_little_name = "igor"
my_big_name = "Igor"
if (my_little_name == your_name) or (my_big_name == your_name):
    print("Hi! I like yours name :D")
else:
    print("Hi! {}".format(your_name))

number = int(input("Send me number"))


def check():
    if number:
        print(number)
    else:
        print("Heyyyo")


check()

print("Now check your cube.")
cube_a = input("What length is A?.")
cube_b = input("What length is B?.")
cube_c = input("What length is C?.")


class Cube:
    def __init__(self, side_length, name):
        self.side_length = side_length
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.side_length == other.side_length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.side_length < other.side_length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.side_length > other.side_length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.side_length <= other.side_length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.side_length >= other.side_length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.side_length != other.side_length


a = Cube(cube_a, "A")
b = Cube(cube_b, "B")
c = Cube(cube_c, "C")

print("1. A == B = {}".format(a == b))
print("1. A == C = {}".format(a == c))
print("1. B == C = {}".format(b == c))

print("2. A < B = {}".format(a < b))
print("2. A < C = {}".format(a < c))
print("2. B < C = {}".format(b < c))

print("3. A > B = {}".format(a > b))
print("3. A > C = {}".format(a > c))
print("3. B > C = {}".format(b > c))

print("4. A <= B = {}".format(a <= b))
print("4. A <= C = {}".format(a <= c))
print("4. B <= C = {}".format(b <= c))

print("5. A >= B = {}".format(a >= b))
print("5. A >= C = {}".format(a >= c))
print("5. B >= C = {}".format(b >= c))

print("6. A != B = {}".format(a != b))
print("6. A != C = {}".format(a != c))
print("6. B != C = {}".format(b != c))

print("Now check your square.")
square_a = input("What length is A?.")
square_b = input("What length is B?.")


class Square:
    def __init__(self, side_length, name):
        self.side_length = side_length
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.side_length == other.side_length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.side_length < other.side_length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.side_length > other.side_length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.side_length <= other.side_length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.side_length >= other.side_length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.side_length != other.side_length


a = Square(square_a, "A")
b = Square(square_b, "B")

print("1. A == B = {}".format(a == b))

print("2. A < B = {}".format(a < b))

print("3. A > B = {}".format(a > b))

print("4. A <= B = {}".format(a <= b))

print("5. A >= B = {}".format(a >= b))

print("6. A != B = {}".format(a != b))


input("Press Enter to continue...")
print("Now check my plants")


class Plant:
    def __init__(self, height, name):
        self.height = height
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.height == other.height

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.height < other.height

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.height > other.height

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.height <= other.height

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.height >= other.height

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.height != other.height


class Flower(Plant):
    def __init__(self, height, name):
        super(Flower, self).__init__(height, name)
        self.height = height
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.height == other.height

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.height < other.height

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.height > other.height

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.height <= other.height

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.height >= other.height

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.height != other.height


class Vegetable(Plant):
    def __init__(self, height, name):
        super(Vegetable, self).__init__(height, name)
        self.height = height
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.height == other.height

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.height < other.height

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.height > other.height

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.height <= other.height

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.height >= other.height

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.height != other.height


class Fruit(Plant):
    def __init__(self, height, name):
        super(Fruit, self).__init__(height, name)
        self.height = height
        self.name = name

    def __eq__(self, other):
        print("Comparision type: {} == {}".format(self.name, other.name))
        return self.height == other.height

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.height < other.height

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.height > other.height

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.height <= other.height

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.height >= other.height

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.height != other.height


plant_one = Plant(10, "Oak")
plant_two = Plant(45, "Pine")

print("1. A == B = {}".format(plant_one == plant_two))
print("2. A < B = {}".format(plant_one < plant_two))
print("3. A > B = {}".format(plant_one > plant_two))
print("4. A <= B = {}".format(plant_one <= plant_two))
print("5. A >= B = {}".format(plant_one >= plant_two))
print("6. A != B = {}".format(plant_one != plant_two))

flower_one = Flower(1, "Rose")
flower_two = Flower(0.2, "Tulip")

print("1. A == B = {}".format(flower_one == flower_two))
print("2. A < B = {}".format(flower_one < flower_two))
print("3. A > B = {}".format(flower_one > flower_two))
print("4. A <= B = {}".format(flower_one <= flower_two))
print("5. A >= B = {}".format(flower_one >= flower_two))
print("6. A != B = {}".format(flower_one != flower_two))

veg_one = Vegetable(0.1, "Onion")
veg_two = Vegetable(0.1, "Potato")

print("1. A == B = {}".format(veg_one == veg_two))
print("2. A < B = {}".format(veg_one < veg_two))
print("3. A > B = {}".format(veg_one > veg_two))
print("4. A <= B = {}".format(veg_one <= veg_two))
print("5. A >= B = {}".format(veg_one >= veg_two))
print("6. A != B = {}".format(veg_one != veg_two))

fruit_one = Fruit(0.12, "Orange")
fruit_two = Fruit(0.011, "Apple")

print("1. A == B = {}".format(fruit_one == fruit_two))
print("2. A < B = {}".format(fruit_one < fruit_two))
print("3. A > B = {}".format(fruit_one > fruit_two))
print("4. A <= B = {}".format(fruit_one <= fruit_two))
print("5. A >= B = {}".format(fruit_one >= fruit_two))
print("6. A != B = {}".format(fruit_one != fruit_two))
