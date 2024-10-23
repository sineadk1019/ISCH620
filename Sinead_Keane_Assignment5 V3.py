
#user input for number of sides/length of sides
# -*- coding: utf-8 -*-
"""
Name: Sinead Keane
Class: ISCH 620
Due Date: 12/3/2023
Assignment #5, Revision 3
Email: sinead.keane001@gmail.com
"""

#In order to do more complex arithmetic (square roots for example) 
#I imported the math module
import math

print("Hello! Welcome to the Shape Assignment. To begin, lets find a \
polygon to review.\n")

#This Class calculates the area, perimeter, and stores the name of a Polygon.
class Polygon:
#this list collects all our shapes    
    shape_list = []
#this initializes the class.    
    def __init__(self, polygon_input, sides_input, length_input):
        self._sides_input = sides_input
        self._length_input = length_input
        self._polygon_input = polygon_input.capitalize() 

#this adds the shape to the shape_list for counting purposes.   
    def shape_name(self,_polygon_input):
        shape = _polygon_input
        self.shape_list.append(shape)
        return shape
#this relays the size of the list when called.
    def shape_size (self):
        return len(self.shape_list)  
#this does all the area calulations when called for specific numbers        
    def polygon_area(self, _sides_input,_length_input):
        if _sides_input == 3:
            h = (.5)*math.sqrt(3)*_length_input
            tri_area = round((0.5*_length_input*h),2)
            return tri_area
        elif _sides_input == 4:
            sqr_area = _length_input**2
            return sqr_area
        elif _sides_input == 5:
            pent_area = round((.25*math.sqrt(5*(5+2*math.sqrt(5)))*_length_input**2),2)
            return pent_area
        elif _sides_input == 6:
            hex_area = (3*math.isqrt(3))/2 * (_length_input**2)
            return hex_area
#this does the perimeter when called.
    def polygon_perim(self, _sides_input, _length_input):
        perim = _sides_input*_length_input
        return perim 
#this function is meant to utilize the above class to pull 3 different shapes. 
#the shapes are then calculated within the class for Area, Perimeter, and List size
#to conclude, the total area and total perimeter is given.
def input_func():
    for x in range(3):
        polygon_input = input("Please name a polygon: ")
        sides_input = int(input("How many sides does your polygon have? (Must be between 3-6 sides.): "))
        if 3<= sides_input <=6: 
            length_input = int(input("What is the length of the side? "))
            if x == 0:
                shape1 = Polygon(polygon_input, sides_input, length_input)
                print(f'\nPolygon name: {shape1.shape_name(polygon_input.capitalize())}\n\
    Polygon list size: {shape1.shape_size()} \n\
    Perimeter: {shape1.polygon_perim(sides_input, length_input)} units\n\
    Area: {shape1.polygon_area(sides_input, length_input)} sq units\n')
            elif x == 1:
                shape2 = Polygon(polygon_input, sides_input, length_input)
                print(f'\nPolygon name: {shape2.shape_name(polygon_input.capitalize())}\n\
    Polygon list size: {shape2.shape_size()} \n\
    Perimeter: {shape2.polygon_perim(sides_input, length_input)} units\n\
    Area: {shape2.polygon_area(sides_input, length_input)} sq units\n')
            elif x == 2:
                shape3 = Polygon(polygon_input, sides_input, length_input)
                print(f'\nPolygon name: {shape3.shape_name(polygon_input.capitalize())}\n\
    Polygon list size: {shape3.shape_size()} \n\
    Perimeter: {shape3.polygon_perim(sides_input, length_input)} units\n\
    Area: {shape3.polygon_area(sides_input, length_input)} sq unit\n\n')
        else:
            print('Please pick a side length between 3 and 6')
            return input_func() 
        
    print(f"The total Area of the three shapes is: \
    {shape1.polygon_area(shape1.sides_input, shape1.length_input)+shape2.polygon_area(shape2.sides_input,shape2.length_input)+shape3.polygon_area(shape3.sides_input,shape3.length_input)} sq units\n") 
    
    print(f'The total perimeter of the three shapes is: \
     {shape1.polygon_perim(shape1.sides_input, shape1.length_input)+shape2.polygon_perim(shape2.sides_input, shape2.length_input)+shape3.polygon_perim(shape3.sides_input, shape3.length_input)} units\n\n')
    
    print(f" Method Call 1: \n\
          Name: {shape1.shape_name(shape1.polygon_input)}\n\
          Perimeter: {shape1.polygon_perim(shape1.sides_input, shape1.length_input)} units\n\
          Area: {shape1.polygon_area(shape1.sides_input, shape1.length_input)} sq units\n") 
    print(f" Method Call 2: \n\
          Name: {shape2.shape_name(shape2.polygon_input)}\n\
          Perimeter: {shape2.polygon_perim(shape2.sides_input, shape2.length_input)} units\n\
          Area: {shape2.polygon_area(shape2.sides_input, shape2.length_input)} sq units \n")
    print(f" Method Call 3: \n\
          Name: {shape3.shape_name(polygon_input.capitalize())}\n\
          Perimeter: {shape3.polygon_perim(shape3.sides_input, shape3.length_input)} units\n\
          Area: {shape3.polygon_area(shape3.sides_input, shape3.length_input)} sq units")

#the function is called with the __main__           
def __main__():
    input_func()
    
__main__()
