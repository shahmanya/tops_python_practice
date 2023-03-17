file=open("tops1.txt","w")
file.write("this is file management demo using python.")
file.close()
print("file written successfully")
print("***********************")


file=open("tops1.txt","r")
print(file.read())
file.close()
print("***********************")

file=open("tops1.txt","a")
file.write("\nNow this file is appended.")
file.close()
print("file appended successfully.")
print("***********************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("***********************")

file=open("tops2.txt","w+")
file.write("this is file w+ mode using pyhton for read/write data.")
print(file.tell())
file.seek(0)
print(file.read())
file.close()
print("**********************************************************************")



file=open("tops2.txt","r+")
print(file.read())
print(file.tell())
file.seek(0)
file.write("\nNow this is r+ mode in new line.")
file.close
print("**********************************************************************")
