from tkinter import *
import tkinter.messagebox as msg
import mysql.connector 

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="python")
print(create_conn())

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("insert status","All fields mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into employee(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("insert status","Data inserted sucessfully")
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")

def search_data():
        e_fname.delete(0,"end")
        e_lname.delete(0,"end")
        e_email.delete(0,"end")
        e_mobile.delete(0,"end")

        if e_id.get()=="":
            msg.showinfo("search status","id is mandatory")
        else:
            conn=create_conn()
            cursor=conn.cursor()
            query="select * from employee where id=%s"
            args=(e_id.get(),)
            cursor.execute(query,args)
            row = cursor.fetchall()
            if row:
                for i in row:
                    e_fname.insert(0,i[1])
                    e_lname.insert(0,i[2])
                    e_email.insert(0,i[3])
                    e_mobile.insert(0,i[4])
            else:
                msg.showinfo("search status","Id is invalid")
            conn.close()
    
def update_data():

    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("update status","all fields mandatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "update employee set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("update status","update successfully")

    e_id.delete(0,"end")
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")
    
    
def delete_data():
    if e_id.get()=="":
        msg.show("delete status","id is mandatory")
    else:
        conn = create_conn()
        cursor= conn.cursor()
        query="delete from employee where id=%s"
        args =(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("delete status","Delete successfully")
    
    e_id.delete(0,"end")
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")
  

root =  Tk()
root.geometry("500x500")
root.title("Employee Registration")
root.resizable(width="false",height="false")

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name:")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last Name:")
l_lname.place(x=50,y=150)

l_email=Label(root,text="Email:")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="Mobile")
l_mobile.place(x=50,y=250)


e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)


insert=Button(root,text="Insert",bg="black",fg="white",font=("Arial,10"),command=insert_data)
insert.place(x=50,y=300)

search=Button(root,text="Search",bg="black",fg="white",font=("Arial,10"),command=search_data)
search.place(x=120,y=300)

update=Button(root,text="Update",bg="black",fg="white",font=("Arial,10"),command=update_data)
update.place(x=190,y=300)

delete=Button(root,text="Delete",bg="black",fg="white",font=("Arial,10"),command=delete_data)
delete.place(x=260,y=300)

