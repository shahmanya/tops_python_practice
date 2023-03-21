#Function with no arguements and no return value

def printline():
    print("*"*50)
printline()
print("Manya Shah")
printline()

#Function with arguement and no return value

def add(a,b):
    print("Addition:",a+b)
printline()
x=int(input("value of x:"))
y=int(input("value of y:"))
add(x,y)
printline()

#

def sub(a,b):
    return a-b
printline()
x=int(input("value of x:"))
y=int(input("value of y:"))
ans=sub(x,y)
print("Subtraction:",ans)
printline()
