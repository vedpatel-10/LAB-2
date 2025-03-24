sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_marks = sub1+sub2+sub3
average_marks = total_marks/3

print("Total marks are:",total_marks)
print("Average marks are:",average_marks)

print("Grade of subject 1 : ")
if sub1<=100 and sub1>=80:    print("O")
elif sub1<=79 and sub1>=70:    print("A+")
elif sub1<=69 and sub1>=60:    print("A")
elif sub1<=59 and sub1>=55:    print("B+")
elif sub1<=54 and sub1>=50:    print("B")
elif sub1<=49 and sub1>=45:    print("C")
elif sub1<=44 and sub1>=40:    print("P")
else:
    print("F")    
    print("You are Failed!")

print("Grade of subject 2 : ")
if sub2<=100 and sub2>=80:    print("O")
elif sub2<=79 and sub2>=70:    print("A+")
elif sub2<=69 and sub2>=60:    print("A")
elif sub2<=59 and sub2>=55:    print("B+")
elif sub2<=54 and sub2>=50:    print("B")
elif sub2<=49 and sub2>=45:    print("C")
elif sub2<=44 and sub2>=40:    print("P")
else:
    print("F")    
    print("You are Failed!")   

print("Grade of subject 3 : ")
if sub3<=100 and sub3>=80:    print("O")
elif sub3<=79 and sub3>=70:    print("A+")
elif sub3<=69 and sub3>=60:    print("A")
elif sub3<=59 and sub3>=55:    print("B+")
elif sub3<=54 and sub3>=50:    print("B")
elif sub3<=49 and sub3>=45:    print("C")
elif sub3<=44 and sub3>=40:    print("P")
else:
    print("F")    
    print("You are Failed!")
    