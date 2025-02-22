import math

#1
degree = float(input("Input degree: "))
radian = degree * math.pi / 180
print("Output radian:", radian)

#2
height = float(input("Height of trapezoid: "))
base1 = float(input("Base first value: "))
base2 = float(input("Base second value: "))
area_trapezoid = ((base1 + base2) / 2) * height
print("Expected Output:", area_trapezoid)

#3
n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area_polygon = (n_sides * side_length * side_length) / (4 * math.tan(math.pi / n_sides))
print("The area of the polygon is:", area_polygon)

#4
base_parallelogram = float(input("Length of base: "))
height_parallelogram = float(input("Height of parallelogram: "))
area_parallelogram = base_parallelogram * height_parallelogram
print("Expected Output:", area_parallelogram)
