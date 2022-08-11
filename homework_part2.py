from module_1 import get_area as a
from module_1 import get_circ as c
print("\n")
length = int(input("How many feet long is your house? "))
width = int(input("How many feet wide is your house? "))

print(a(length, width))
print("\n")

radius = int(input("What is the radius of your circle? "))
units = input("In what units? ")

print(c(radius, units))