


import random
import math
print("Do you have the radius or diameter?")
choice = input()
if choice == "radius":
    print("Please input the radius")
    radius = input()
    b = float(radius)
    print(math.pi*(b**2))
elif choice == "diameter":
    print("Please input the diameter")
    diameter = input()
    a = float(diameter)
    print(math.pi*a)