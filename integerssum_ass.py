x=int(input("Enter a value of x:"))
y=int(input("Enter a value of y:"))
z=int(input("Enter a value of z:"))

sum=x+y+z

if x==y or y==z or z==x:
    print("Sum of integers is 0")

else:
    print("Sum of integers is:",sum)
