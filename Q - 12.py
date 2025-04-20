import math

radius =int(input("Enter the radius: "))
x1 = int(input("Enter X coordinate of centre: "))
y1 = int(input("Enter Y coordinate of centre: "))

x2 = int(input("Enter X coordinate of point: "))
y2 = int(input("Enter Y coordinate of point: "))

a = pow(x2-x1,2)
b = pow(y2-y1,2)

distance = math.sqrt(a + b)
if distance == radius:
    print("Point lies on the circle.")
elif distance > radius:
    print("Point lies outside the circle.")
else :
    print("Point lies inside the circle.")

#OUTPUT:
# Enter the radius: 7
# Enter X coordinate of centre: 0
# Enter Y coordinate of centre: 0
# Enter X coordinate of point: 9
# Enter Y coordinate of point: -3
# Point lies outside the circle.    
