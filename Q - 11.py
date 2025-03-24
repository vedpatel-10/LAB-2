x1= int(input("Enter x1: "))
y1= int(input("Enter y1: "))
x2= int(input("Enter x2: "))
y2= int(input("Enter y2: "))
x3= int(input("Enter x3: "))
y3= int(input("Enter y3: "))

'''
 Here lets assume these cordinates form a triangle,
if area is zero, then they are collinear otherwise not
'''
area =(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)) / 2

if area == 0:
    print("Points fall on one staright line")

else :
    print("Points do not fall on straight line")

