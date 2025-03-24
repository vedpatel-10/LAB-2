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

