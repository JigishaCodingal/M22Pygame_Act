from tkinter import *
T=Tk()
T.title("My window")
T.geometry("300x200")



f1=Frame(master=T)
f1.place(x=0,y=0)

btn=Button(master=f1,text="Click Me",fg="red")
btn.pack()

f2=Frame(master=T,bg="yellow",bd=5,relief=RIDGE,height=100,width=200)
f2.place(x=150,y=100)

L=Label(master=f2,text="HAMMAD")
L.pack()
