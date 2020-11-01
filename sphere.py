"""
Program:  Sphere
Author: Matthew Shover

This program will calculate the diameter, circumference, surface area and volume of the sphere.
It will ask the user to enter the radius and display the results up to the second number after the decimal place.
"""

import math

pi = math.pi

sphere = float(input("Enter the sphere's radius : "))

radius = sphere
diameter = 2 * radius
circumference = pi * diameter
surfaceArea = 4 * pi * radius * radius
volume = 4/3 * pi * radius * radius * radius

print("Diameter      : ",round(diameter,2))
print("Circumference : ",round(circumference,2))
print("surface area  : ",round(surfaceArea,2))
print("volume        : ",round(volume,2))
