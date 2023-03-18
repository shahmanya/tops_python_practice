num=int(input("Enter number:"))
n1,n2,n3=0,1,2
print("Fiboonaci Series:",n1,n2,n3, end=" ")
for i in range(3,num):
    n4=n1+n2+n3
    n1=n2
    n2=n3
    n3=n4
    print(n4, end=" ")
print()
    
    
