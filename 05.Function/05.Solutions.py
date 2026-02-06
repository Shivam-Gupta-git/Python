import math

radius = int(input("Please enter radius to calculate the 'area' and 'circumference': "))

def circle(radius) :
  area = round((math.pi * (radius ** 2)), 2)
  circumfrences = round((2 * math.pi * radius), 2)
  return area, circumfrences

a, b = circle(radius)
print("area and circumfrence of given radius",radius, "is area:",a, "and  circumfrence:",b)