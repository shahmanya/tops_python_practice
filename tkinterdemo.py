from tkinter import * #tkinter module
import mysql.connector #mysql connector library pip install mysql-connector-python
import tkinter.messagebox as msg 

#to connect database

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_example"
        )
#insert data to table in database
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert status","All field is mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")
        msg.showinfo("Insert Status","Data Inserted Successfully")
    

root=Tk() #object of Tk class
root.geometry("400x380")
root.title("my tkinter example")
root.resizable(width=False,height=False)

#lable creation
l_id=Label(root,text="ID",font=("Arial",15))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",15))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME",font=("Arial",15))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",15))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("Arial",15))
l_mobile.place(x=50,y=250)

#Textbox creation(Entry)
e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root)
e_fname.place(x=200,y=100)

e_lname=Entry(root)
e_lname.place(x=200,y=150)

e_email=Entry(root)
e_email.place(x=200,y=200)

e_mobile=Entry(root)
e_mobile.place(x=200,y=250)

#Button Creation
insert=Button(root,text="INSERT",font=("Arial",10),fg="white",bg="black",command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="SEARCH",font=("Arial",10),fg="white",bg="black")
search.place(x=110,y=300)

update=Button(root,text="UPDATE",font=("Arial",10),fg="white",bg="black")
update.place(x=178,y=300)

delete=Button(root,text="DELETE",font=("Arial",10),fg="white",bg="black")
delete.place(x=244,y=300)
