'''
AUTHOR: ELLEN JOY
DATE:30/11/2024
PROGRAM TO CHECK WHETHER THE SIDES ARE OF A RIGHT ANGLE TRIANGLE
'''



def is_right_angle_triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2== sides[0]**2 + sides[1]**2:
        return True
    return False
side1=int(input("Enter a side 1 of the triangle:"))
side2=int(input("Enter a side  2 of the triangle:"))
side3=int(input("Enter a side 3 of the triangle:"))
if is_right_angle_triangle(side1,side2,side3):
     print("The given sides are part of the right angle triangle")
else:
     print("The given sides are not a part of the right angle triangle")


