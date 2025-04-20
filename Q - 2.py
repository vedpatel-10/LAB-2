x = int(input("What is X ? :"))
y = int(input("What is Y ? :"))
z = int(input("What is Z ? :"))

 # checking for largest number 
if x>z and x>y:
    print("Largest number is",x)
elif y>z and y>x:
    print("Largest number is",y) 
else:
    print("Largest number is",z)    

# checking for smallest number 
if x<y and x<z :
    print("Smallest number is",x)
elif y<z and y<x :
    print("Smallest number is",y)
else :
    print("Smallest number is",z)        

#OUTPUT:
# What is X ? :32
# What is Y ? :53
# What is Z ? :2
# Largest number is 53
# Smallest number is 2 
