1.
import math
def degree_to_radian(degree):
    radian = degree * (math. pi / 180)
    return radian

# Пример
degree_needed = 15
radian_needed = degree_to_radian(degree_needed)
print(f"{degree_needed} degree is equal to {radian_needed:.5f} radian")

2.
def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area


height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))


area = trapezoid_area(height, base1, base2)


print("Expected Output:", area)
3.
import math

def regular_polygon_area(num_sides, side_length):
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    
    area = 0.5 * num_sides * side_length * apothem
    
    return area

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = regular_polygon_area(num_sides, side_length)

print("The area of the polygon is:", area)

4.
def parallelogram_area(base_length, height):
    area = base_length * height
    return area

base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base_length, height)

print("Expected Output:", area)
