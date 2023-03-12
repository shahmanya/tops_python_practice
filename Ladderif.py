sname=input("Enter Student Name:")
rno=int(input("Enter Rollno.:"))
s1=int(input("Enter Subject1 Marks:"))
s2=int(input("Enter Subject2 Marks:"))
s3=int(input("Enter Subject3 Marks:"))

total=s1+s2+s3
per=total/3

print("Student Name:",sname)
print("Student Rollno:",rno)
print("Total Marks:",total)
print("Percentage:",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("Firstclass")
elif per>=50:
    print("SecondClass")
elif per>=40:
    print("Pass")
else:
    print("Fail")
