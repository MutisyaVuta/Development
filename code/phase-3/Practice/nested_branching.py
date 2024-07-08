x= int(input("Enter a value for X:  "))
y= int(input("Enter a value for Y:  "))

if x==y:
    print("X and Y are EQUAL")
    if y != 0:
        print("hence,x/y is", x/y)
elif x<y:
    print("X is smaller")
else:
    print("Y is smaller")

print("End of program")
