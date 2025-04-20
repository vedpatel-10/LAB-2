L = int(input("Enter length of rectangle: "))
B = int(input("Enter breadth of rectangle: "))
P = 2*(L+B)
A = L*B 

print("Perimeter of rectangle is",P)
print("Area of rectangle is",A)

if A>P:
    print("Area is greater than Perimeter")
else:
    print("Perimeter is greater than Area")

#OUTPUT:
# Enter length of rectangle: 20
# Enter breadth of rectangle: 12
# Perimeter of rectangle is 64
# Area of rectangle is 240
# Area is greater than Perimeter  
