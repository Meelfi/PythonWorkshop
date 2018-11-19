#!/usr/bin/env python3
print("What is your name?")
name = input()
print("What is your Surname?")
surname = input()
print("What is your Age?")
age = input()
print("Hey {} {} your age is {}".format(name, surname, age))
print("{}! Please input number".format(name))
number = float(input())
print("Hey. Your lucky number is {}".format(number))


class Flower:
    def __init__(self, flower_type, flower_name, color, size):
        self.flower_type = flower_type
        self.flower_name = flower_name
        self.color = color
        self.size = size
        print("Your {} name is {}. This flower color is {} and size {}cm.".format(self.flower_type, self.flower_name, self.color, self.size))


print("What type flower do you like")
flower_prefer = input()
print("What do you name this flower")
flower_globalname = input()
print("What color is this flower")
flower_color = input()
print("What size is this flower (in cm)")
flower_size = input()
flower = Flower(flower_prefer, flower_globalname, flower_color, flower_size)
