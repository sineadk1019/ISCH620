# -*- coding: utf-8 -*-
"""
Name: Sinead Keane
Class: ISCH 620
Due Date: 12/3/2023
Assignment #5
Email: sinead.keane001@gmail.com
"""

#Three class instances - Area, Perimeter, Add Values to lists, 
# Return the name, area, perimeter


# Assume the number of sides is 3<= X <= 6

#3 instances = total area and total perimeter

#user input for number of sides/length of sides
import math

def input_func ():
    polygon_input = input("Please name a polygon: ")
    sides_input = int(input("How many sides does your polygon have? (Must be between 3-6 sides.): "))
    length_input = int(input("What is the length of the side? "))

class Polygon():
    # area of a polygon = 1/2 perimeter x apothem
    # apothem = side length / 2*tan(pi/number of sides)
    # perimeter of a polygon = number of sides x side length 
    def __init__(polygon_input, sides_input, length_input):
        self.name = polygon_input
    def polygon_area(self, sides_input, length_input):
        if sides_input == "3":
            tri_area = (math.sqrt(3)*length_input**2)/4
            print(f"{polygon_input} has an area of {tri_area}.")
        elif sides_input == "4":
            square_area = lenght_input**2
            print(f"{polygon_input} has an area of {square_area}.")
        elif sides_input == "5":
            pen_area = .75*math.sqrt(5)*(5+2*math.sqrt(5)) * side_length**2
            print(f"{polygon_input} has an area of {pen_area}.")
        elif sides_input == "6":
            hex_area = (3*math.sqrt(3))/2 * (length_input**2)
            print(f"{polygon_input} has an area of {hex_area}.")
        else:
            print("Please pick a side length between 3 and 6")
            return input_func()
        def polygon_perim(sides_input, length_input):
            ctr = 0
            tri_perim = sides_input*length_input
            ctr = ctr + 1
            print(f"{polygon_input} has a perimeter of {tri_perim}./n/n This is shape {ctr}")

        self.area = polygon_area()
        self.perim = polygon_perim()
        
        
    
    
class myshape
def __init__(a,b,c)
self.name=a
def printname(self)
print(self.name)
new_shape=myshape()
new_shape.printname()
class Toy(object):
    
    shape1.area, shape2.area, shape3.area = total area, then do total perimeter same. 


quiz 5 - drunkards walk, random, probability, regression, stats chapter/ machine learning probs, vocabulary. 