num = int(input("Enter a number: "))
digit = 0

# convert negative number to positive
if num <0 :
    num = -1 *num

if num>=0 and num<=9:
    digit =1

if num>=10 and num<=99:
    digit =2

if num>=100 and num<=999:
    digit = 3

if num>=1000 and num<=9999:
    digit = 4

if num>=10000 and num<=99999:
    digit = 5
                
if num>=100000 and num<=999999:
    digit = 6

if num>=1000000 and num<=9999999:
    digit = 7

if num>=10000000 and num<=99999999:
    digit = 8

if num>=100000000 and num<=999999999:
    digit = 9 

if num>=1000000000 and num<=9999999999:
    digit = 10
    
print("Number of digits:",digit)

